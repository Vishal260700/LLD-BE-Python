"""
Decorator pattern is responsible for adding dynamic improvements on existing objects to further decouple these base objects and improvements
"""

"""
Coffe House system with support for beverages and addons like double cream, caramel, milk, etc
"""

"""
Use Cae (Flow) - 
1. Customer comes up
2. Asks for a certain base beverage
3. Puts on certain number of add ons to it
4. get cash details for it and checkout
5. Order confirmation
"""

"""
System Requirements - 
1. Beverage Selection
2. Update order with Add-ons
3. Get Bill after order confirmation
"""

"""
Classes - 
1. Beverage (Abstract class)
    params - 
    Beverage Name (string)
    Beverage Price (integer)

2. Decorator (Abstract Class) [extends Beverage]
    params - 
    Decorator Name ~ Beverage Name (String)
    Decorator Price ~ Beverage Price (integer)

3. Order
    params - 
    orderId - uuid
    Beverages - Array<Beverage>
    Price - integer

3. CoffeHouse
    params - 
    registeredBeverages (Object) [set]
    registeredAddOns (Object) [set]
    orders Array<Order>

"""

"""
Code Implementation
"""

"""
Abstract Beverage Class
"""
from abc import ABC, abstractmethod
class Beverage(ABC):

    """
    Init @ Beverage
    """
    def __init__(self, name, price):
        # protected so only extended classes can access
        self._name = name
        self._price = price
    
    """
    Name @ Beverage
    """
    def getName(self):
        return self._name
    
    """
    Price @ Beverage
    """
    def getPrice(self):
        return self._price

"""
Main Beverages i.e. Base Beverages
"""
class Espresso(Beverage):
    def __init__(self):
        super().__init__("Espresso", 10)
    
class Cappuccino(Beverage):
    def __init__(self):
        super().__init__("Cappuccino", 20)

class Latte(Beverage):
    def __init__(self):
        super().__init__("Latte", 15)

"""
Abstract Decorator Class
"""
class Decorator(Beverage):
    def __init__(self, name, price):
        super().__init__(name, price)
       
"""
Add Ons
"""
class Milk(Decorator):

    # Take a Base Beverage as constructor input
    def __init__(self, beverage):
        self.beverage = beverage
    
    # Override
    def getName(self):
        return self.beverage.getName() + " with milk "
    
    # Override
    def getPrice(self):
        return self.beverage.getPrice() + 2

class Caramel(Decorator):

    # Take a Base Beverage as constructor input
    def __init__(self, beverage):
        self.beverage = beverage
    
    # Override
    def getName(self):
        return self.beverage.getName() + " with caramel "
    
    # Override
    def getPrice(self):
        return self.beverage.getPrice() + 4


class Cream(Decorator):

    # Take a Base Beverage as constructor input
    def __init__(self, beverage):
        self.beverage = beverage
    
    # Override
    def getName(self):
        return self.beverage.getName() + " with cream "
    
    # Override
    def getPrice(self):
        return self.beverage.getPrice() + 7

"""
Order Status Enum
"""
from enum import Enum
class OrderStatus(Enum):
    COOKING, DELIVERED = 1, 2

"""
Order
"""
import uuid
class Order:
    def __init__(self, beverage):
        self.__id = str(uuid.uuid4())
        self.__beverage = beverage
        self.__status = OrderStatus.COOKING
    
    def orderReady(self):
        self.__status = OrderStatus.DELIVERED
    
    def getOrderDetails(self):
        print("Order Id: {ID} with Beverage: {beverageDetails} for a price {beveragePrice} is with status of {status}".format(ID=self.__id, beverageDetails=self.__beverage.getName(), beveragePrice=str(self.__beverage.getPrice()), status=self.__status))

"""
CoffeHouse
"""
class CoffeHouse:
    def __init__(self):
        self.__registeredBeverages = set(["ESPRESSO", "LATTE", "CAPPUCCINO"])
        self.__registeredAddOns = set(["CARAMEL", "MILK", "CREAM"])
        self.__orders = []
    
    def getOrderSummary(self):
        for order in self.__orders:
            order.getOrderDetails()
    
    def takeOrder(self, orderDetails):
        for orderDetail in orderDetails:
            baseBeverage = orderDetail[0]
            addOns = orderDetail[1]
            if(baseBeverage in self.__registeredBeverages):
                if(baseBeverage == "ESPRESSO"):
                    order = Espresso()
                elif(baseBeverage == "LATTE"):
                    order = Latte()
                elif(baseBeverage == "CAPPUCCINO"):
                    order = Cappuccino()
                else:
                    print("Internal error, missing class entity")
            else:
                print("Beverage not available in coffe house: {Beverage}".format(Beverage=baseBeverage))
                continue
            for addOn in addOns:
                if(addOn in self.__registeredAddOns):
                    if(addOn == "CARAMEL"):
                        order = Caramel(order)
                    elif(addOn == "MILK"):
                        order = Milk(order)
                    elif(addOn == "CREAM"):
                        order = Cream(order)
                    else:
                        print("Internal error, missing class entity")
                else:
                    print("addOn not available in coffe house: {addOn}".format(addOn=addOn))
            order = Order(order)
            order.getOrderDetails()
            self.__orders.append(order)
    
"""
Testing
"""

coffeHouse = CoffeHouse()
orderDetails = [["ESPRESSO", ["MILK", "CREAM"]], ["LATTE", ["MILK", "CARAMEL"]]]
coffeHouse.takeOrder(orderDetails)
print("****************************************************************")
coffeHouse.getOrderSummary()