"""
Builder Pattern - Builder pattern is defined for building up object with 
"""

"""
Problem Statement - Factory for making Laptops of different brands with different specifications
"""

"""
Use Case Flow -
1. System is requested for a Laptop of a brand with specifications (in terms of prod code)
2. The Object for appropriate object should be created
"""

"""
System Requirement -
1. Request for different laptop brands
2. Each laptop brand can have different support for parts
"""

"""
Classes - 
1. DeviceBuilder - Interface
    params - 
    mouse (protected)
    keyboard (protected)
    screen (protected)
    methods - (abstract public)
    setMouse
    setKeyboard
    setScreen
    showSpecs
2. DellDeviceBuilder - implements DeviceBuilder
    methods - 
    setMouse
    setKeyboard
    setScreen
    showSpecs
3. HpDeviceBuilder - implements DeviceBuilder
    methods - 
    setMouse
    setKeyboard
    setScreen
    showSpecs
4. SystemDirector 
    methods - 
    buildDesktop (params -> DeviceBuilder) (return - Desktop)
"""

"""
Code Implementation
"""

from abc import ABC, abstractmethod
class DeviceBuilder(ABC):

    """
    Init @ DeviceBuilder
    """
    def __init__(self):
        self._mouse = None
        self._keyboard = None
        self._screen = None
    
    """
    Abstract Methods @ DeviceBuilder
    """

    @abstractmethod
    def setMouse(self, mouse):
        pass
    
    @abstractmethod
    def setKeyboard(self, keyboard):
        pass
    
    @abstractmethod
    def setScreen(self, screen):
        pass

    @abstractmethod
    def showSpecs(self):
        pass

class DellDeviceBuilder(DeviceBuilder):

    """
    Init @ DellDeviceBuilder
    """
    def __init__(self):
        super().__init__()
    
    def setMouse(self, mouse):
        self._mouse = mouse
    
    def setKeyboard(self, keyboard):
        self._keyboard = keyboard
    
    def setScreen(self, screen):
        self._screen = screen
    
    def showSpecs(self):
        print("DELL: PRODUCT")
        print("MONITOR: " + self._screen)
        print("KEYBOARD: " + self._keyboard)
        print("MOUSE: " + self._mouse)


class HpDeviceBuilder(DeviceBuilder):

    """
    Init @ HpDeviceBuilder
    """
    def __init__(self):
        super().__init__()
    
    def setMouse(self, mouse):
        self._mouse = mouse
    
    def setKeyboard(self, keyboard):
        self._keyboard = keyboard
    
    def setScreen(self, screen):
        self._screen = screen
    
    def showSpecs(self):
        print("HP: PRODUCT")
        print("MONITOR: " + self._screen)
        print("KEYBOARD: " + self._keyboard)
        print("MOUSE: " + self._mouse)

class SystemDirector:
    """
    Init @ SystemDirector
    """
    def __init__(self):
        self.brands = set()
        self.__deviceBuilder = None

    """
    Brands @ SystemDirector
    """
    def addBrand(self, newBrand):
        self.brands.add(newBrand)
    
    def removeBrand(self, brand):
        self.brands.remove(brand)
    
    """
    getDeviceBuilder (private) @ SystemDirector - responsible for solely getting appropriate device builder
    """
    def __getDeviceBuilder(self, brandCode):
        if(brandCode in self.brands):
            if(brandCode == "DELL"):
                return DellDeviceBuilder()
            elif(brandCode == "HP"):
                return HpDeviceBuilder()
            else:
                print("Builder not found")
                return None
        else:
            raise Exception("Unregistered brand")

    """
    BuildDesktop (public) @ SystemDirector - responsible for creating the desktop
    """
    def buildDesktop(self, brandCode, deviceCode):
        self.__deviceBuilder = self.__getDeviceBuilder(brandCode)
        # based on deviceCode we get mouse, keyboard, screen configs (pass deviceCode as param in set methods altogether) for now we use dummy values
        self.__deviceBuilder.setKeyboard(brandCode + " KEYBOARD 123")
        self.__deviceBuilder.setMouse(brandCode + "  KEYBOARD 123")
        self.__deviceBuilder.setScreen(brandCode + "  KEYBOARD 123")
        self.__deviceBuilder.showSpecs()

"""
Testing
"""

director = SystemDirector()
director.addBrand("DELL")
director.addBrand("HP")
director.buildDesktop("DELL", "1234")
director.buildDesktop("HP", "1234")
