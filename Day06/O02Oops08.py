
# equal is mandatory, overload one more comparison oprtr
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __eq__(self, other):                # it work's for not equal to also
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary   # it work's for less than also

emp1 = Employee("Jack", 25000)
print(emp1)

print("-" * 40)
emp2 = Employee("Kurt", 30000)
print(emp2)

print("-" * 40)
if emp1 == emp2:
    print(f"{emp1.name}'s salary {emp1.salary} is NOT equal to {emp2.name}'s salary {emp2.salary} ")
else:
    print(f"{emp1.name}'s salary {emp1.salary} is equal to {emp2.name}'s salary {emp2.salary} ")

print("-" * 40)

if emp1 < emp2:
    print(f"{emp1.name}'s salary {emp1.salary} is less than {emp2.name}'s salary {emp2.salary} ")
else:
    print(f"{emp1.name}'s salary {emp1.salary} is greater than {emp2.name}'s salary {emp2.salary} ")

print("-" * 40)
if emp1 >= emp2:
    print(f"{emp1.name}'s salary {emp1.salary} is less than or equal to {emp2.name}'s salary {emp2.salary} ")
else:
    print(f"{emp1.name}'s salary {emp1.salary} is greater than or equal to {emp2.name}'s salary {emp2.salary} ")