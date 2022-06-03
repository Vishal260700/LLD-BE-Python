import uuid
class Redis:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.value = {}
    
    def get(self, mainKey):
        # key not found
        if(mainKey not in self.value):
            return None
        # key, value send as paid or arrays
        keys = []
        values = []
        for key in self.value[mainKey].keys():
            keys.append(key)
            values.append(self.value[mainKey][key])
        return [keys, values]

    def put(self, mainKey, keys, values):
        # new mainkey init it
        if(mainKey not in self.value):
            self.value[mainKey] = {}
        
        # first check existing datatypes are same or not
        for i in range(0, len(keys)):
            if(keys[i] in self.value[mainKey] and type(self.value[mainKey][keys[i]]) != type(values[i])):
                return "Data Type Error"
        
        # put data in key of main key
        for i in range(0, len(keys)):
            self.value[mainKey][keys[i]] = values[i]
        
        return None

    def keys(self):
        return sorted(self.value.keys())
    
    def delete(self, key):
        if(key in self.value):
            del self.value[key]

    def search(self, attrKey, attrVal):
        res = []
        for key in self.value.keys():
            if(attrKey in self.value[key] and self.value[key][attrKey] == attrVal):
                res.append(key)
        return sorted(res)