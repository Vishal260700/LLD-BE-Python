from Redis import Redis
class Driver:
    def __init__(self):
        # main object
        redis = Redis()
        # driver commands
        while(True):
            commands = input().split(" ")
            if(commands[0] == "get"):
                getRes = redis.get(commands[1])
                if(getRes != None):
                    keys = getRes[0]
                    values = getRes[1]
                    for i in range(0, len(keys)):
                        print("{key}: {value},".format(key=keys[i], value=values[i]), end=" ")
                    print("")
            elif(commands[0] == "put"):
                mainKey = commands[1]
                keys = []
                values = []
                for i in range(2, len(commands)):
                    if(i%2 == 0):
                        key = commands[i]
                        keys.append(key)
                    else:
                        value = commands[i]
                        values.append(value)
                redis.put(mainKey, keys, values)
            elif(commands[0] == "delete"):
                mainKey = commands[1]
                redis.delete(mainKey)
            elif(commands[0] == "keys"):
                keys = redis.keys()
                for key in keys:
                    print("{key},".format(key=key), end=" ")
                print("")
            elif(commands[0] == "search"):
                attrKey = commands[1]
                attrVal = commands[2]
                keys = redis.search(attrKey, attrVal)
                for key in keys:
                    print("{key},".format(key=key), end=" ")
                print("")
            else:
                break

Driver()