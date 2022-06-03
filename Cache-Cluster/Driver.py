# The goal of the exercise is to create a class that manages a cluster of caches.
from CacheCluster import CacheCluster

cluster = CacheCluster()
cluster.put("1", "key", "value")
print(cluster.get("1", "key")) # This should return "value"
cluster.put("1", "key1", "value1")
print(cluster.get("1", "key1")) # This should return "value1"
cluster.put("2", "key", "value")
print(cluster.get("2", "key")) # This should return  "value"

cluster.replicate("1", "2")
print(cluster.get("2", "key1")) # This should return "value1"
cluster.replicate("2", "3")
cluster.replicate("3", "2")
cluster.put("3", "jack", "silq")
print(cluster.get("2", "jack"))
print(cluster.get("3", "key1")) # This should return "value1"
cluster.put("1", "new_key", "new_value")
print(cluster.get("2", "new_key"))
print(cluster.get("3", "new_key"))