""""
Observer Pattern  is decribed as an pattern where we have heirarchial entitites of one to many relationships. 
For example youtube subscribers getting messages of new video drop from the creator i.e. subscribed users are observer to changes in the publishers portfolio
"""

"""
Problem Statement - Design a system where notifications are sent to employees in such a way that when CEO msgs everyone gets it
BU head messages there employees get it and when employees message it only the team members of his gets it
"""

"""
Use Case Flow - 
1. CEO Messages into the system
2. Employees are notified with the message

1. BU Head messages into the system
2. Employees are notified with the message of that Buisness team

1. Employee add in a message into the system
2. Team members are notified with the message
"""

"""
System Requirements - 
1. Add Subscriber
2. Remove Subscriber
3. Notify Subscribers with a message
"""

"""
Main Entities in the system - 
1. Employee Class
    Emp Name
    Team - Team (Nullable)

2. CEO Class extends Employee Class
    Emp Name (from base class)
    Subscribers - Array<Employee>

3. Manager Class extends Employee Class
    Emp Name (from base class)
    Subscribers - Array<Employee>

4. Team Class
    Members - Array<Employee>

5. Message Class
    Message - String
    From - Employee
"""

"""
Code Implementation
"""


# Message.py
class Message:
    """
    Init @ Message
    """
    def __init__(self, frm, msg):
        self.__sender = frm
        self.__msg = msg
    
    """
    sender @ Message
    """
    def getSender(self):
        return self.__sender
    
    """
    msg @ Message
    """
    def getMsg(self):
        return self.__msg

# Team.py
class Team:
    
    """
    Init @ Team
    """
    def __init__(self, teamName):
        self.__teamName = teamName
        self.__members = {} # Key - EmpId, Value - Employee
    
    """
    TeamName @ Team
    """
    def getTeamName(self):
        return self.__teamName

    """
    Member @ Team
    """
    def addMember(self, member):
        self.__members[member.getId()] = member
    
    def removeMember(self, memberId):
        del self.__members[memberId]

    """
    Notify @ Team
    """
    def notify(self, message):
        for member in self.__members:
            self.__members[member].notify(message)

# Employee.py
import uuid
class Employee:

    """
    Init @ Employee
    """
    def __init__(self, empName, team=None):
        self.__id = str(uuid.uuid4())
        self.__isActive = True
        self.__name = empName
        self.__team = team
    
    """
    ID @ Employee
    """
    def getId(self):
        return self.__id

    """
    Activity @ Employee
    """
    def deactivateUser(self):
        self.__isActive = False
    
    def activateUser(self):
        self.__isActive = True

    """
    Name @ Employee
    """
    def getName(self):
        return self.__name
    
    """
    Team @ Employee
    """
    def getTeam(self):
        return self.__team
    
    def setTeam(self, team):
        self.__team = team
    
    """
    Notify @ Employee
    """
    def notify(self, message):
        if(self.__isActive):
            print("Recieved message from {sender} to {recipient} with message: {message}".format(sender=message.getSender(), recipient=self.__name, message=message.getMsg()))

# CEO.py
class CEO(Employee):

    """
    Init @ CEO
    """
    def __init__(self, name):
        super().__init__(name)
        self.__subscribers = {} # Key - empId
    
    """
    Notifying @ CEO
    """
    def notify(self, msg):
        for sub in self.__subscribers:
            message = Message(self.getName(), msg)
            self.__subscribers[sub].notify(message)
    
    """
    Subscribers @ CEO
    """
    def addSubscriber(self, employee):
        self.__subscribers[employee.getId()] = employee
    
    def removeSubscriber(self, employeeId):
        del self.__subscribers[employeeId]

# Manager.py
class Manager(Employee):
    """
    Init @ Manager
    """
    def __init__(self, name, team):
        super().__init__(name, team)
    
    """
    NotifyTeam @ Manager
    """
    def notifyTeam(self, msg):
        message = Message(self.getName(), msg)
        self.getTeam().notify(message)

# NotificationSystem.py
class NotificationSystem:
    """
    Init @ NotificationSystem
    """
    def __init__(self):
        self.__members = {}
        pass
    
    """
    Notifying @ NotificationSystem
    """
    def notify(self, senderId, msg):
        sender = self.__members.get(senderId)
        sender.notify(msg)
    
    """
    Members @ NotificationSystem
    """
    def addMember(self, newEmployee):
        self.__members[newEmployee.getId()] = newEmployee

    def removeMember(self, memberId):
        del self.__members[memberId]

"""
Testing
"""

notificationSystem = NotificationSystem()

"""
Executive level
"""
ceo = CEO("Sundar Pichai")

"""
Teams
"""
Nest = Team("Nest")
Maps = Team("Maps")
Pay = Team("Pay")

"""
Managers with assigned Teams (Nest managed by 2 managers)
"""
manager1 = Manager("Manager 1", Nest)
manager11 = Manager("Manager 11", Nest)
manager2 = Manager("Manager 2", Maps)
manager3 = Manager("Manager 3", Pay)

ceo.addSubscriber(manager1)
ceo.addSubscriber(manager11)
ceo.addSubscriber(manager2)
ceo.addSubscriber(manager3)

"""
Employees
"""
emp1 = Employee("emp1")
emp2 = Employee("emp2")
emp3 = Employee("emp3")
emp5 = Employee("emp5")
emp4 = Employee("emp4")
emp6 = Employee("emp6")
emp7 = Employee("emp7")
emp8 = Employee("emp8")
emp9 = Employee("emp9") # no team assigned

ceo.addSubscriber(emp1)
ceo.addSubscriber(emp2)
ceo.addSubscriber(emp3)
ceo.addSubscriber(emp4)
ceo.addSubscriber(emp5)
ceo.addSubscriber(emp6)
ceo.addSubscriber(emp7)
ceo.addSubscriber(emp8)
ceo.addSubscriber(emp9)

Nest.addMember(emp1)
Nest.addMember(emp2)
Nest.addMember(emp3)

Pay.addMember(emp4)
Pay.addMember(emp5)

Maps.addMember(emp6)
Maps.addMember(emp7)
Maps.addMember(emp8)

ceo.notify("Message from CEO here")
manager1.notifyTeam("Message from manager 1 here")
manager2.notifyTeam("Message from manager 2 here")
manager3.notifyTeam("Message from manager 3 here")
manager11.notifyTeam("Message from manager 11 here")