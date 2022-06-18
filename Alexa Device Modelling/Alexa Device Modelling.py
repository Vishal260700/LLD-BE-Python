"""
Design OOPs for Amazon Alexa devices.
Echo Show, Echo Dot and, Amazon Echo. These devices have different input(typing, voice), output(sound, display) and power(battery, plug-in) mode. 
Your Design should be able to handle different input & must respond with the correct output when Alexa is asked about its battery status(i.e X% charged or plugged-in).
"""

"""
Follow up questions - 
1. So we have in total 3 types of devices enabling Alexa correct? And we can have additional added to this list later?
2. Input types are 2 - Type and voice correct? Any other type of input that we need to look for?
3. Power is subjective as in some devices can be battery operated some charge on the go, how do we want to show/reply to such queries?
4. Any other alexa functionality support required other than battery query? If yes then we can keep those methods abstract and can implement them later on. Is it okay?
"""

"""
Use Case Flow - 
1. Based on the device type a certain input type is registered
2. The input type can be classified into query types for now simple conditional will work but later an ml model can help us in this.
3. The input type is redirected to appropriate method to take care of the query and output is given based on the input Type only.
"""

"""
System Requirements - 
1. Alexa Class (Main object for the system) 
2. Devices like echo show,echo dot, echo classes for certain charecterestics specfic to them
3. Input Type (enums)
4. Power status in % or charging status (True or False)
5. Test Cases
"""

"""
Classes -
1. AlexaDevice (Abstract)
    params -
    batteryStatus - Enum (Charging or not)
    methods -
    getBatteryStatus - abstract
    setBatteryStatus - public method
    generateOutput - protected method

2. Echo extends AlexaDevice
    params -
    batteryPercentage - float ([0, 1])
    methods -
    setBatteryPercentage - public
    getBatteryStatus - public

3. Echo show extends AlexaDevice
    params -
    batteryPercentage - float ([0, 1])
    methods -
    setBatteryPercentage - public
    getBatteryStatus - public

3. Echo dot extends AlexaDevice
    params - (same as extended class)
    methods -
    getBatteryStatus - public
"""

"""
Code Implementation
"""

# BatteryStatus.py
from enum import Enum
class BatteryStatus(Enum):
    CHARGING, NOTCHARGING = 1, 2

# InputType.py
from enum import Enum
class InputType(Enum):
    TYPE, VOICE = 1, 2

# RegisteredQuery.py
from enum import Enum
class RegisteredQuery(Enum):
    BATTERY, WELCOME, UNKNOWN = 1, 2, 3

# OutputType.py - required for many times we get type input but require output type in voice as well as in type
from enum import Enum
class OutputType(Enum):
    DISPLAY, SOUND = 1, 2

# Query.py - pre processing performed by ML Model which gives classifiedMsg
class Query:
    """
    Init @ Query
    """
    def __init__(self, classifiedMsg, inputType):
        self.__classifiedMsg = classifiedMsg
        self.__inputType = inputType
    """
    RegisteredQuery @ Query
    """
    def getMessage(self):
        return self.__classifiedMsg
    """
    InputType @ Query
    """
    def getInputType(self):
        return self.__inputType

# AlexaDevice.py
from abc import ABC, abstractmethod
class AlexaDevice(ABC):
    """
    Init @ AlexaDevice
    """
    def __init__(self, batteryStatus=BatteryStatus.NOTCHARGING):
        self._batteryStatus = batteryStatus
    
    """ 
    BatteryStatus (public) @ AlexaDevice
    """
    def setBatteryStatus(self, batteryStatus):
        self._batteryStatus = batteryStatus

    @abstractmethod
    def _getBatteryStatus(self):
        pass
    
    """
    Output (protected) @ AlexaDevice
    """
    @abstractmethod
    def _displayOutput(self, outputMsg):
        pass
    
    @abstractmethod
    def _speakOutput(self, outputMsg):
        pass

    """
    Supported Messages(protected) @ AlexaDevice
    """
    def _getWelcomeMessage(self):
        return "Hi, Welcome to Amazon {deviceName}, ask me anything :)"

    def _getDefaultMessage(self):
        return "Sorry, I didn't get it please try again!!"
    
    """
    Generate Output (private) @ Alexa Device
    """
    def __generateOutput(self, queryClassfication, outputType):
        if(outputType == OutputType.DISPLAY):
            if(queryClassfication == RegisteredQuery.BATTERY):
                self._displayOutput(self._getBatteryStatus())
            elif(queryClassfication == RegisteredQuery.WELCOME):
                self._displayOutput(self._getWelcomeMessage())
            elif(queryClassfication == RegisteredQuery.UNKNOWN):
                self._displayOutput(self._getDefaultMessage())
        elif(outputType == OutputType.SOUND):
            if(queryClassfication == RegisteredQuery.BATTERY):
                self._speakOutput(self._getBatteryStatus())
            elif(queryClassfication == RegisteredQuery.WELCOME):
                self._speakOutput(self._getWelcomeMessage())
            elif(queryClassfication == RegisteredQuery.UNKNOWN):
                self._speakOutput(self._getDefaultMessage())
        else:
            raise Exception("unknown output type format: %s" % outputType)

    """
    Ingest Query (public) @ AlexaDevice
    """
    def ingestQuery(self, Query):
        if(Query.getInputType() == InputType.TYPE):
            self.__generateOutput(Query.getMessage(), OutputType.DISPLAY)
        elif(Query.getInputType() == InputType.VOICE):
            self.__generateOutput(Query.getMessage(), OutputType.SOUND)
        else:
            raise Exception("unknown input type format: %s" % Query.getInputType())

# Echo.py
import math
class Echo(AlexaDevice):
    """
    Init @ Echo
    """
    def __init__(self, batteryStatus=BatteryStatus.NOTCHARGING, batteryPercentage=0.17):
        self.__batteryPercentage = batteryPercentage
        super().__init__(batteryStatus)
    
    """
    BatteryPercentage @ Echo
    """
    def __getBatteryPercentage(self):
        return math.floor(self.__batteryPercentage*100)

    """
    Abstract Method implementations @ Echo
    """
    def _speakOutput(self, outputMsg):
        print("Speaking Echo Output: {outputMsg}".format(outputMsg=outputMsg))
    
    def _displayOutput(self, outputMsg):
        self._speakOutput(outputMsg) # can't display so redirect to speak functionality

    def _getBatteryStatus(self):
        if(self._batteryStatus == BatteryStatus.NOTCHARGING):
            return "Alexa Device Echo is charged at {batteryPercentage} percentage".format(batteryPercentage=self.__getBatteryPercentage())
        else:
            return "Alexa Device Echo is plugged in and is currently charged upto {batteryPercentage} percentage".format(batteryPercentage=self.__getBatteryPercentage())

# EchoShow.py
import math
class EchoShow(AlexaDevice):
    """
    Init @ EchoShow
    """
    def __init__(self, batteryStatus=BatteryStatus.NOTCHARGING, batteryPercentage=0.37):
        self.__batteryPercentage = batteryPercentage
        super().__init__(batteryStatus)
    
    """
    BatteryPercentage @ EchoShow
    """
    def __getBatteryPercentage(self):
        return math.floor(self.__batteryPercentage*100)
    
    """
    Abstract Method implementations @ Echo Show
    """
    def _displayOutput(self, outputMsg):
        print("Displaying Echo Show Output: {outputMsg}".format(outputMsg=outputMsg))
    
    def _speakOutput(self, outputMsg):
        print("Speaking Echo Show Output: {outputMsg}".format(outputMsg=outputMsg))

    def _getBatteryStatus(self):
        if(self._batteryStatus == BatteryStatus.NOTCHARGING):
            return "Alexa Device Echo Show is charged at {batteryPercentage} percentage".format(batteryPercentage=self.__getBatteryPercentage())
        else:
            return "Alexa Device Echo Show is plugged in and is currently charged upto {batteryPercentage} percentage".format(batteryPercentage=self.__getBatteryPercentage())

# EchoDot.py
import math
class EchoDot(AlexaDevice):
    """
    Init @ EchoDot
    """
    def __init__(self, batteryStatus=BatteryStatus.NOTCHARGING):
        super().__init__(batteryStatus)
    
    """
    Abstract Method implementations @ Echo Dot
    """
    def _speakOutput(self, outputMsg):
        print("Speaking Echo Dot Output: {outputMsg}".format(outputMsg=outputMsg))
    
    def _displayOutput(self, outputMsg):
        self._speakOutput(outputMsg) # can't display so redirect to speak functionality

    def _getBatteryStatus(self):
        if(self._batteryStatus == BatteryStatus.NOTCHARGING):
            return "Echo Dot is not plugged in" # unrealistic wont give any output tho
        else:
            return "Echo Dot is plugged In"


"""
Testing
"""

batteryQuery1 = Query(RegisteredQuery.BATTERY, InputType.VOICE)
batteryQuery2 = Query(RegisteredQuery.BATTERY, InputType.TYPE)

echoDeviceNotCharging = Echo()
echoDeviceCharging = Echo(BatteryStatus.CHARGING)

echoDeviceNotCharging.ingestQuery(batteryQuery1)
echoDeviceCharging.ingestQuery(batteryQuery1)
echoDeviceNotCharging.ingestQuery(batteryQuery2)
echoDeviceCharging.ingestQuery(batteryQuery2)

print("********************************")

echoShowDeviceNotCharging = EchoShow()
echoShowDeviceCharging = EchoShow(BatteryStatus.CHARGING, 0.7)

echoShowDeviceNotCharging.ingestQuery(batteryQuery1)
echoShowDeviceCharging.ingestQuery(batteryQuery1)
echoShowDeviceNotCharging.ingestQuery(batteryQuery2)
echoShowDeviceCharging.ingestQuery(batteryQuery2)

print("********************************")

echoDotDeviceNotCharging = EchoDot()
echoDotDeviceCharging = EchoDot(BatteryStatus.CHARGING)

echoDotDeviceNotCharging.ingestQuery(batteryQuery1)
echoDotDeviceCharging.ingestQuery(batteryQuery1)
echoDotDeviceNotCharging.ingestQuery(batteryQuery2)
echoDotDeviceCharging.ingestQuery(batteryQuery2)

print("********************************")