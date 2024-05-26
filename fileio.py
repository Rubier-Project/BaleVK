import os

class FileIO(object):
    def __init__(self, path: str | bytes = None) -> None:
        self.fp = path

    def existsStat(self):
        if self.fp == None:
            return False
        
        else:
            return os.path.exists(self.fp)
        
    def isFile(self):
        if self.fp == None:
            return False
        
        else:
            return os.path.isfile(self.fp)
        
    def isDir(self):
        if self.fp == None:
            return False
        
        else:
            return os.path.isdir(self.fp)
        
    def listDir(self):
        os.chdir(self.fp)
        if self.fp == None:
            return []
        
        else:
            return os.listdir(self.fp)
        
    def changeDir(self):
        if self.fp == None:
            return False
        
        else:
            if self.existsStat():
                if self.isDir():
                    os.chdir(self.fp)
                    return True
                else:return False
            else:return False

    def readStream(self):
        if self.fp == None:
            return False
        
        else:
            if self.existsStat():
                if self.isFile():
                    return open(self.fp, 'rb')
                else:return False
            else:return False