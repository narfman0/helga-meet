import sys
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock
from mongomock import MongoClient
sys.modules['helga.plugins'] = mock.Mock()  # hack to avoid py3 errors in test
from helga.db import db


class Testmeet(unittest.TestCase):
    def setUp(self):
        self.db_patch = mock.patch(
            'pymongo.MongoClient',
            new_callable=lambda: MongoClient
        )
        self.db_patch.start()
        self.addCleanup(self.db_patch.stop)

    def tearDown(self):
        db.meet.drop()
        db.meet.meetup.drop()
        db.meet.entries.drop()

    def test_meet_simple(self):
        from helga_meet.helga_meet import status, schedule, remove
        # TODO add schedule checker to verify PSA was called
        test1 = {
            'channel': 'channel1',
            'name': 'test1',
            'participants': 'psa @all',
            'cron_interval': {'seconds': '1'},
        }
        schedule(**test1)
        status(test1['name'], 'n1', 's1')
        self.assertTrue(db.meet.entries.find().count() > 0)
        result = db.meet.meetup.find_one({'name': test1['name']})
        self.assertEqual(test1['name'], result['name'])
        remove(test1['name'], True)
        self.assertFalse(db.meet.meetup.find().count() > 0)
        self.assertFalse(db.meet.entries.find().count() > 0)


if __name__ == '__main__':
    unittest.main()
