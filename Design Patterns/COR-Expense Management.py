"""
Chain of Resposibility Design Pattern - For something of workflow (choices are there)
"""

""""
Problem Statement - To create a Expense management application on CMD
"""

"""
Use Case (Flow) - 
1. We will have expenses report send to the system
2. It needs to be approved or rejected by the person in charge
3. Rejection based on some params
4. Acceptance will be based on current person's ability to judge and power
5. If not in the ability to do so - send to higher level person (until we hit a roof then we reject automatically)
"""

"""
System Requirements - (Based on Use Case)
1. Ability to upload a expense report
2. Ability to Reject a report
3. Ability to approve a report
4. Ability to pass on the report
"""

"""
Main Entities in the System - 
1. Approver (Level Wise)
2. System
3. Expense Report
"""

"""
Class Attributes

Approver
    - Manager (Nullable)
    - Name (varChar i.e. String)
    - approveLimit (integer, NonNullable)

Expense Report
    - Amount (integer)
    - ID (String)
    - Status (enum)

System
    - Approvers
    - Expense Reports
"""

""""
Code Implementation
"""

# ReportStatus.py
from enum import Enum
class ReportStatus(Enum):
    PENDING, APPROVED, REJECTED = 1, 2, 3

# ExpenseReport.py
import uuid
class ExpenseReport:
    """
    Init @ Report
    """
    def __init__(self, amount, status=ReportStatus.PENDING):
        self.__amount = amount # only get
        self.__id = str(uuid.uuid4()) # only get
        self.__status = status # both get and set
    
    """
    ID @ Report
    """
    def getId(self):
        return self.__id
    
    """
    Status @ Report
    """
    def getStatus(self):
        return self.__status

    def approveReport(self):
        self.__status = ReportStatus.APPROVED
    
    def rejectReport(self):
        self.__status = ReportStatus.REJECTED
    
    """
    Amount @ Report
    """
    def getAmount(self):
        return self.__amount

# AbstractApprover.py
import uuid
from abc import ABC, abstractmethod
class AbstractApprover(ABC):
    
    """
    Init @ AbstractApprover
    """
    def __init__(self, name, limit, manager=None):
        self._id = str(uuid.uuid4()) # protected (type - string)
        self._name = name # protected (type - string)
        self._manager = manager # protected (type - AbstractApprover)
        self._approveLimit = limit
    
    """
    ID @ AbstractApprover
    """
    def getId(self):
        return self._id
    
    """
    Name @ AbstractApprover
    """
    def getName(self):
        return self._name
    
    """
    Manager @ AbstractApprover
    """
    def getManager(self):
        return self._manager
    
    def setManager(self, newManager):
        self._manager = newManager
    
    """
    ApproveLimit @ AbstractApprover
    """
    def getLimit(self):
        return self._approveLimit

    """
    Abstract Method - Overide by child classes
    """
    def evaluateReport(self, report):
        pass

# Manager.py
class Manager(AbstractApprover):

    def __init__(self, name, manager):
        super().__init__(name, 1000, manager)
    
    def evaluateReport(self, report):
        if(isinstance(report, ExpenseReport)):
            if(report.getAmount() > self.getLimit()):
                self.getManager().evaluateReport(report)
            else:
                # default approvals
                report.approveReport()
                print("Report Id: {repId} Processed and approved by {name} for cost: {cost}".format(repId=report.getId(), name=self.getName(), cost=report.getAmount()))
            return None
        else:
            raise Exception("Incorrect item for procesing")

# Director.py
class Director(AbstractApprover):

    def __init__(self, name):
        super().__init__(name, 10000, None)
    
    def evaluateReport(self, report):
        if(isinstance(report, ExpenseReport)):
            if(report.getAmount() > self.getLimit()):
                if(self.getManager() is None):
                    print("Report out of range")
                else:
                    self.getManager().evaluateReport(report)
            else:
                # default approvals
                report.approveReport()
                print("Report Id: {repId} Processed and approved by {name} for cost: {cost}".format(repId=report.getId(), name=self.getName(), cost=report.getAmount()))
            return None
        else:
            raise Exception("Incorrect item for procesing")

# ExpenseManager.py
class ExpenseManager:
    def __init__(self):
        self.__managers = {}
        self.__directors = {}

    def createDirector(self, name):
        newDirector = Director(name)
        self.__directors[newDirector.getId()] = newDirector
        return newDirector.getId()
    
    def createManager(self, name, directorId):
        newManager = Manager(name, self.__directors[directorId])
        self.__managers[newManager.getId()] = newManager
        return newManager.getId()
    
    def processReport(self, report, approverId):
        if(approverId in self.__managers):
            approver = self.__managers[approverId]
            approver.evaluateReport(report)
        else:
            raise Exception("Incorrect Approver Id")

expenseManager = ExpenseManager()
directorId = expenseManager.createDirector("director")
managerId = expenseManager.createManager("manager", directorId)

dummyReport = ExpenseReport(100)
expenseManager.processReport(dummyReport, managerId)

dummyReport = ExpenseReport(1000)
expenseManager.processReport(dummyReport, managerId)

dummyReport = ExpenseReport(5000)
expenseManager.processReport(dummyReport, managerId)

dummyReport = ExpenseReport(500000)
expenseManager.processReport(dummyReport, managerId)