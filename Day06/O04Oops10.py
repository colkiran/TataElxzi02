
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'NodeJS', 'AngularJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        # return self.tech.__iter__()
        return iter(self.tech)


emp1 = Employee("Mike", 45000)
print(emp1)

print("-" * 40)
print(len(emp1))

print("-" * 40)
print([t for t in emp1])
