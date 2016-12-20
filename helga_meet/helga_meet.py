from datetime import datetime
import json

import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from helga.db import db
from helga.plugins import command, random_ack
from helga import settings

_client = None


def status(name, nick, status):
    db.meet.entries.add({
        'name': name,
        'nick': nick,
        'status': status,
        'time': datetime.utcnow(),
    })


def schedule(name, channel, participants, schedule):
    db.meet.meetup.update({
        {'name': name},
        {"$set": {
            "channel": channel,
            "participants": participants,
            "schedule": schedule,
        }},
        True,
    })


def remove(name):
    db.meet.meetup.delete_many({'name': name})
    db.meet.entries.delete_many({'name': name})


@command('meet', help='System for asynchronous meetings e.g. standup')
def meet(client, channel, nick, message, cmd, args):
    global _client
    _client = client
    if args[0] == 'status':
        status(args[1], nick, args[2:])
        return nick + ": " + random_ack()
    if args[0] == 'schedule':
        name = args[1]
        s = args[4:]  # schedule arguments, e.g. "days 1"
        status(name, args[2], args[3], dict(zip(s[::2], s[1::2])))
        add_meeting_scheduler(name)
        return random_ack()
    if args[0] == 'remove':
        if nick in settings.operators:
            remove(args[1])
            return random_ack()
        return "Sorry " + nick + ", you don't have permission to do that"
    return "I don't understand this meet request"


def add_meeting_scheduler(name):
    schedule_kwargs = db.meet.meetup.find_one({'name': name})['schedule']
    scheduler.add_job(
        func=lambda: meeting_monitor(name),
        trigger=CronTrigger(**schedule_kwargs),
        id='meeting_monitor_' + name,
        replace_existing=True)


def meeting_monitor(name):
    """ Regularly run task to trigger meeting reminders """
    global _client
    if not _client:
        return
    meetup = db.meet.meetup.find_one({'name': name})
    _client.msg(meetup['channel'], meetup['participants'] + ': ' + meetup['channel'])


scheduler = BackgroundScheduler()
scheduler.start()
atexit.register(lambda: scheduler.shutdown())
for meeting in db.meet.meetup.find():
    add_meeting_scheduler(meeting['name'])
