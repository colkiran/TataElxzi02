
# Aithmetic Operators Magic Method
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 =Employee("Jack", 25000)
print(emp1)

emp2 = Employee("Shiva",8000)
print(emp2)

print("-"*50)

print("ADD = ",emp1 + emp2)
print("SUB = ",emp1 - emp2)
print("Mul = ",emp1 * emp2)
print("Div = ",emp1 / emp2)
print("floor Div = ",emp1 // emp2)


