helga-meet
==============

.. image:: https://badge.fury.io/py/helga-meet.png
    :target: https://badge.fury.io/py/helga-meet

.. image:: https://travis-ci.org/narfman0/helga-meet.png?branch=master
    :target: https://travis-ci.org/narfman0/helga-meet

System for asynchronous meetings e.g. standup

Installation
------------

Install via pip::

    pip install helga-meet

And add to settings!

Usage
-----

Note: Every time you restart helga with preexisting meetings, you must use the meet
command to initialize the scheduler! It can be a dummy command like ``!meet foobar``
that isn't recognized, as long as it hits the meet plugin.

Schedule a daily standup at 3pm Mon-Fri, saying in room #general: "PSA @all"::

    !meet schedule standup "#general" "PSA @all" "hour 15 day_of_week 0-4"

The above final argument is a cron formatted group of kwargs.

Adds a status entry for the day for the user. Nick and time saved along with status::

    !meet status standup made widget1, started on widget2. will finish widget2, and no blockers

Then, we can query for digests of certain date ranges. The start and end date ranges
should be quoted, and are kwargs of datetime::

    !meet digest standup "year 2016 month 12 day 1" "year 2016 month 12 day 30"

To get a list of all current meetups::

    !meet dump

To remove a particular meetup (assuming you are an OPERATOR)::

    !meet remove test1

And if you want to remove all associated status update along with the meetup::

    !meet remove test1 entries

Development
-----------

Install all the testing requirements::

    pip install -r requirements_test.txt

Run tox to ensure everything works::

    make test

You may also invoke `tox` directly if you wish.

Release
-------

To publish your plugin to pypi, sdist and wheels are (registered,) created and uploaded with::

    make release

License
-------

Copyright (c) 2016 Jon Robison

See LICENSE for details
