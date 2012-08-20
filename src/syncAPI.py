"""
The SyncBox API will handle all actions and such that need be performed
by the SyncBox application.

"""

class SyncAPI(object):
    """
    API for SyncBox, and the _only_ way to execute commands and access the
    SyncBox internals.
    
    The instances has a shared state, because there is no need to have multiple
    states.
     
    """
    
    __state = {
        '_watchList': {}
    }
    
    def __init__(self):
        """
        Instantiate and set up the API object. 
        
        Since the object should always share it's state, we set the __dict__
        variable to the class variable __state.
        
        """
        self.__dict__ = self.__state

    @property
    def watchList(self):
        """Getter for the watchList attribute"""
        return self._watchList
    
    @watchList.setter
    def watchList(self, value):
        """Getter for the watchList attribute"""
        self._watchList = value
    
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

