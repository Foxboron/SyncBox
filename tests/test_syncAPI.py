"""
Testing src/syncAPI

"""

import unittest
import src.syncAPI


class SyncAPITest(unittest.TestCase):
    """Test the SyncAPI class methods"""

    def setUp(self):
        """Set up the test"""
        self.syncAPI = src.syncAPI.SyncAPI()

    def test_watchList_returns_a_dictionary(self):
        """Test the getter for _watchList"""
        self.assertEqual(self.syncAPI.watchList(), {})

    def test_SetWatchList_sets_the_watchList_attribute(self):
        """Test the setter for _watchList"""
        watchList = {'foo': 'bar'}
        self.syncAPI.setWatchList(watchList)
        self.assertEqual(self.syncAPI.watchList(), watchList)

    def test_CrawlDirectory_returns_a_dictionary_with_a_directory_tree(self):
        """Test crawlDirectory"""
        pass

    def test_WatchDirectory_adds_a_directory_to_the_watchList(self):
        """Test watchDirectory"""
        pass

    def test_WatchFile_adds_a_file_to_the_watchList(self):
        """Test watchFile"""
        pass


if __name__ == '__main__':
    unittest.main()
