"""
The SyncBox API will handle all actions and such that need be performed
by the SyncBox application.

"""

class SyncAPI(object):
    """
    API for SyncBox, and the _only_ way to execute commands and access the
    SyncBox internals.
     
    """
    
    def __init__(self):
        """Instantiate and set up the API object"""
        pass

    def setWatchList(self, watchList):
        """Setter for _watchList"""
        self._watchList = watchList

    def watchList(self):
        """Getter for _watchList"""
        try:
            return self._watchList
        except AttributeError:
            self.setWatchList({})
            return self._watchList
    
    def crawlDirectory(self, path):
        """
        Crawl a directory and return a dictionary with files and their data
        """
        pass
    
    def watchDirectory(self, path):
        """Add a directory to the watch list"""
        pass
    
    def watchFile(self, filePath):
        """Add a file to the watch list"""
        pass

