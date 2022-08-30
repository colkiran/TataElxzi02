
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):

    def doJob(self):
        print("Developers Job......")


def BankJob(emp):
    print("BankJob Started.......")
    emp.doJob()
    print("BankJob Ended.......")
    print("-" * 40)
    
Mike = Manager()
David = Developer()

BankJob(Mike)
BankJob(David)
