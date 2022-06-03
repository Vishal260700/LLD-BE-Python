# /*
# NOTE: Feel free to google any syntactical specifics during the interview.
# For the purposes of this exercise, consider a cache to be a hashmap/object.
# Sample skeleton:

from collections import defaultdict
from Cache import Cache
class CacheCluster:
    def __init__(self):
        self.caches = {} # cacheId: Cache
        self.relations = {} # cacheId - master: [replicaCacheIds]
        pass
    
    # helper function
    def validateCacheId(self, cacheId):
        if(cacheId in self.caches):
            return True
        return False

    # BFS Approach to replicate values in all cache relations
    def overrideSingleValue(self, cacheId, key, value, visited):
        self.caches[cacheId].put(key, value)
        visited.add(cacheId)
        if(self.validateRelationKey(cacheId)):
            for replicaId in self.relations[cacheId]:
                if(not replicaId in visited):
                    self.overrideSingleValue(replicaId, key, value, visited)

    # Adds or updates the cache with a key with the provided value. Note that
    # the cache_id is required here as well since the class is managing a list of
    # caches.
    def put(self, cache_id, key, value):
        # making a new cache node
        # cacheID present or not
        if(not self.validateCacheId(cache_id)):
            self.caches[cache_id] = Cache(cache_id)
        if(self.validateRelationKey(cache_id)):
            visited = set()
            self.overrideSingleValue(cache_id, key, value, visited)
        else:
            self.caches[cache_id].put(key, value)
        pass
    
    # Gets a value with the provided key.  Note that the cache_id is required
    # her as well since the class is managing a list of caches.
    def get(self, cache_id, key):
        # point where cacheId is required
        if(not self.validateCacheId(cache_id)):
            return 
        return self.caches[cache_id].get(key)
        pass

    # helper function
    def validateRelationKey(self, cacheId):
        if(cacheId in self.relations):
            return True
        return False

    # This function has to copy over all data from cache with id:
    # master_cache_id to cache with id: replica_cache_id. Subsequent puts to master should automatically write through to the replica
    def replicate(self, master_cache_id, replica_cache_id):
        ## check if the relation causes a cycle
        if( not self.validateRelationKey(master_cache_id)):
            self.relations[master_cache_id] = []

        if(not replica_cache_id in self.relations[master_cache_id]):
            if(not self.validateCacheId(replica_cache_id)):
                self.caches[replica_cache_id] = Cache(replica_cache_id)
            self.relations[master_cache_id].append(replica_cache_id)
            self.overrideValues(master_cache_id, replica_cache_id)
        pass
    
    def overrideValues(self, masterCache, replicaCache):
        masterData = self.caches[masterCache].data
        for key in masterData.keys():
            val = masterData[key]
            self.caches[replicaCache].put(key, val)