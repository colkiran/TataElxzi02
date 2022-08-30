
class Employee:

    def __init__(self, name):
        self.__name = name         # Private Variable

    def __str__(self):
        return f"Name is {self.__name}"

emp1 = Employee("Kevin Costner")
print(emp1)

print("-" * 40)
# print(emp1._Employee__name)
print(emp1.__dict__)
emp1._Employee__name = "Steve Smith"
print(emp1)