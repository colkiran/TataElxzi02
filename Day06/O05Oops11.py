
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'NodeJS', 'AngularJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, ind):
        return self.tech[ind]

    def __setitem__(self, ind, val):
        self.tech[ind] = val


emp1 = Employee("Kevin", 85000)
print("-" * 40)
print([t for t in emp1])

print("-" * 40)
emp1.append("Python")
print([t for t in emp1])

print("-" * 40)
res = emp1[3]
print(f"res :{res}")

print("-" * 40)
emp1[3] = "Java_Script"
print([t for t in emp1])

