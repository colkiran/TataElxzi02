
# over-riding the parent class constructor

class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def __init__(self):                 # Over_riding
        super().__init__()              # call the parent class constructor
        print("Bird Ctor.....")
        self.weight = '1 kg'

    def fly(self):
        print("Birds fly......")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 40)
print(cuckoo.__dict__)