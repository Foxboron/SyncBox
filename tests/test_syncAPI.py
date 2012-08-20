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
    
    def test_syncAPI_has_a_shared_state(self):
        """Test the shared state of the syncAPI class"""
        firstInstance = src.syncAPI.SyncAPI()
        secondInstance = src.syncAPI.SyncAPI()
        # Make sure their not the same object
        self.assertNotEqual(firstInstance, secondInstance)
        # Set the watchList property and check it is the same in both instances
        firstInstance.watchList = {'biz': 'baz'}
        self.assertEqual(firstInstance.watchList, secondInstance.watchList)

    def test_the_watchList_property_can_be_set_and_get(self):
        """Test the setter for _watchList"""
        watchList = {'foo': 'bar'}
        self.syncAPI.watchList = watchList
        self.assertEqual(self.syncAPI.watchList, watchList)

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
