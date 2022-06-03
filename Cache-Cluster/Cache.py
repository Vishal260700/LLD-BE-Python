class Cache:
    def __init__(self, cacheId):
        self.cacheId = cacheId
        self.data = {} # string: {string, timeStamp}
    
    def validateKey(self, key):
        if(key in self.data):
            return True
        return False

    def put(self, key, value):
        if(self.validateKey(key)):
            self.data[key] = value
        else:
            self.data[key] = value
    
    def get(self, key):
        if(self.validateKey(key)):
            return self.data[key]
        return None