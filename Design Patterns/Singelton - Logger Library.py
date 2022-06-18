""""
Singelton Pattern suggests having a strict single instance of an class, examples - DBClients responsible for CRUD on DB
DefaultManagementService responsible for accessing and updating platform specific variables
"""

"""
CAUTION :- Thread Safety is of utmost importance in this pattern
"""

"""
Problem Statement - Implement a logger for a system with single instance everywhere in the service
"""

"""
Use Case Flow -
1. Application use the logger instance to log a message
2. The message is stored in appropriate location as per message config
3. Only single instance of logger is allowed
"""

"""
System Requirements
1. Single instance of logger
2. Sink to specific locations as per level
3. Message type supported - FATAL, ERROR, INFO, WARN
4. Message Time Stamp
"""

"""
Classes 

1. Logger
    params -
    instanceCount integer (strict upto 1) [Singelton]
    sinkPaths - HashMap (Key - OriginType, Value - DestinationPath) [nested hashmap - 2 level]
    methods -
    warn(message: Message) [public] [based on Message.origin and methodType redirect to log method with appropriate path]
    error(message: Message) [public]
    info(message: Message) [public]
    fatal(message: Message) [public]
    log(msg: string, path: string) [private] [opens file and write to file]

2. Message
    params -
    msg: string
    origin: integer (1,2,3 -> DB, File, console)
    TimeStamp: DateTime : GMT Format

3. Log 
    methods - 
    getLogger - return Logger Instance (same everytime) with thread safety

"""

"""
Code Implementation
"""

# MessageOrigin.py
from enum import Enum
class MessageOrigin(Enum):
    DB, FILE, CONSOLE = 1, 2, 3

# MessageType.py
from enum import Enum
class MessageType(Enum):
    WARN, ERROR, FATAL, INFO = 1, 2, 3, 4

# Message.py
import time
class Message:
    """
    Init @ Message
    """
    def __init__(self, msg, origin):
        self.__msg = msg
        self.__origin = origin
        self.__time = time.time()
    """
    message @ Message
    """
    def getMessage(self):
        return self.__msg
    """
    Origin @ Message
    """
    def getOrigin(self):
        return self.__origin
    """
    Time @ Message
    """
    def getTime(self):
        return self.__time

# Logger.py
class Logger:
    """
    Init @ Logger
    """
    instances = 0
    def __init__(self):
        Logger.instances += 1
        self.__sinkPaths = {
            MessageType.WARN: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            },
            MessageType.ERROR: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            },
            MessageType.FATAL: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            },
            MessageType.INFO: {
                MessageOrigin.DB: [],
                MessageOrigin.FILE: [],
                MessageOrigin.CONSOLE: []
            }
        }
    """
    Warn @ Logger
    """
    def warn(self, message):
        self.__log(message, MessageType.WARN)
    """
    Info @ Logger
    """
    def info(self, message):
        self.__log(message, MessageType.INFO)
    """
    Error @ Logger
    """
    def error(self, message):
        self.__log(message, MessageType.ERROR)
    """
    Fatal @ Logger
    """
    def fatal(self, message):
        self.__log(message, MessageType.FATAL)
    """
    Log (private) @ Logger
    """
    def __log(self, message, msgType):
        self.__sinkPaths.get(msgType).get(message.getOrigin()).append(message.getMessage() + " " + str(message.getTime()) + " instance Number: " + str(Logger.instances))
    
    def getLogs(self):
        for msgType in self.__sinkPaths.keys():
            for msgOrigin in MessageOrigin:
                logs = self.__sinkPaths[msgType][msgOrigin]
                for log in logs:
                    print(log)

# Log.py
import threading 
class Log:

    """
    Init @ Log
    """
    def __init__(self):
        self.__loggerInstance = None

    """
    Get Logger @ Log
    """
    def getLogger(self):
        # Double locking for unnecessary lock uncalled for - optimization
        if(self.__loggerInstance is None):
            lock = threading.Lock()
            lock.acquire()
            if(self.__loggerInstance is None):
                self.__loggerInstance = Logger()
            lock.release()
        return self.__loggerInstance

"""
Testing
"""
log = Log()
logger = log.getLogger()
warnMessage = Message("warning message", MessageOrigin.DB)
logger.warn(warnMessage)
warnMessage = Message("warning message", MessageOrigin.CONSOLE)
logger.warn(warnMessage)

infoMessage = Message("info message", MessageOrigin.CONSOLE)
logger.info(infoMessage)
warnMessage = Message("info message", MessageOrigin.FILE)
logger.info(infoMessage)
logger.getLogs()