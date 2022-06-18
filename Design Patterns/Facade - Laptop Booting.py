"""
Facade Pattern - Only show the Front of the Application, not the background processing, example - Booting of Laptop
hides complexity of the application that happens behind the scenes
loose coupling between subsystems and its clients
"""

"""
Problem Statement - Laptop Booting check (first 10-15 seconds of laptop bootings)
"""

"""
Use Case Flow - 
1. User click on ON button (Hardware input)
2. Hardware Checks - 
    MotherBoard
    Memory
    Battery
3. Software Checks - 
    OS
    Driver
4. If all checks are ok - boot successfully else fail
"""

"""
Main Entities - 
1. MotherBoard
2. Memory
3. Battery
4. OS
5. Driver
6. Software Checker
7. Hardware Checker
8. DeviceChecker (Facade)
"""

"""
Class Attributes - 
1. MotherBoard
    method
    checkMotherBoardOnBoot : boolean
2. Memory
    method
    checkMemoryOnBoot : boolean
3. Battery
    method
    checkBatteryOnBoot : boolean
4. HardWareChecker
    params
    motherBoard: MotherBoard
    memory: Memory
    battery: Battery
    method
    checkHardwareOnBoot : boolean
5. OS
    method
    checkOSOnBoot : boolean
6. Driver
    method
    checkDriverOnBoot : boolean
7. SoftwareChecker
    params
    os: OS
    driver: Driver
    method
    checkSoftwareOnBoot : boolean
8. DeviceChecker
    params
    hardwareChecker: HardWareChecker
    softwareChecker: SoftwareChecker
    methods
    checkDeviceOnBoot: boolean
"""

"""
Code Implementation
"""

# MotherBoard.py
class MotherBoard:

    def __init__(self):
        pass

    def checkMotherBoardOnBoot(self):
        print("Mother Board Check in progress")
        return True

# Memory.py
class Memory:

    def __init__(self):
        pass

    def checkMemoryOnBoot(self):
        print("Memory Check in progress")
        return True

# Battery.py
class Battery:

    def __init__(self):
        pass

    def checkBatteryOnBoot(self):
        print("Battery Check in progress")
        return True

# HardWareChecker.py
class HardWareChecker:

    def __init__(self):
        self.__motherBoard = MotherBoard()
        self.__memory = Memory()
        self.__battery = Battery()

    def checkHardwareOnBoot(self):
        self.__motherBoard.checkMotherBoardOnBoot()
        self.__memory.checkMemoryOnBoot()
        self.__battery.checkBatteryOnBoot()
        print("Hardware Check Complete")
        return True

# OS.py
class OS:

    def __init__(self):
        pass

    def checkOSOnBoot(self):
        print("Operating system check in progress")
        return True

# Driver.py
class Driver:

    def __init__(self):
        pass

    def checkDriverOnBoot(self):
        print("Driver check in progress")
        return True

# SoftWareChecker.py
class SoftWareChecker:

    def __init__(self):
        self.__os = OS()
        self.__driver = Driver()

    def checkSoftwareOnBoot(self):
        self.__os.checkOSOnBoot()
        self.__driver.checkDriverOnBoot()
        print("Software Check Complete")
        return True

# DeviceChecker.py
class DeviceChecker:
    def __init__(self):
        self.__hardware = HardWareChecker()
        self.__software = SoftWareChecker()
    
    def checkDeviceOnBoot(self):
        self.__hardware.checkHardwareOnBoot()
        self.__software.checkSoftwareOnBoot()
        print("Device Checks Complete")
        return True

# Client.py
class Client:
    def __init__(self):
        self.__deviceChecker = DeviceChecker()

    def DeviceBootUp(self):
        self.__deviceChecker.checkDeviceOnBoot()

"""
Testing
"""
client = Client()
client.DeviceBootUp()