import sys
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock
from mongomock import MongoClient
sys.modules['helga.plugins'] = mock.Mock()  # hack to avoid py3 errors in test
from helga.db import db
from helga_meet.helga_meet import status, schedule, remove


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

    def test_meet_simple(self):
        # TODO add schedule checker to verify PSA was called
        test1 = {
            'channel': 'channel1',
            'name': 'test1',
            'participants': 'psa @all',
            'schedule': 'seconds 1',
        }
        schedule(**test1)
        status({'name': test1['name'], 'nick': 'n', 'status': 's1'})
        self.assertTrue(len(db.meet.entries.find()) > 0)
        result = db.meet.meetup.find_one({'name': test1['name']})
        self.assertEqual(test1['name'], result['name'])
        remove(test1['name'])
        self.assertFalse(len(db.meet.meetup.find()) > 0)
        self.assertFalse(len(db.meet.entries.find()) > 0)


if __name__ == '__main__':
    unittest.main()
