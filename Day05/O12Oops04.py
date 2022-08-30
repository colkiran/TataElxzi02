
class Player:

    def __init__(self, name, age):                         # constructor
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 38)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 35)
ply2.get_details()

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")

ply2.runs = 145
print("-" * 40)
print(f"ply2 :{ply2.__dict__}")

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")
