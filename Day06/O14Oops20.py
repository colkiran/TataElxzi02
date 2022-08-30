
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    def deposit(self):
        pass

class Savings(Account):

    def withDraw(self):
        print("Amount debited from the account......")

    def get_balance(self):
        print("Balance in the account is  ######.##")

sav = Savings()
sav.deposit()
sav.get_balance()

