
class Animal:
    def __init__(self):
        print("Animal Ctor......")

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("fun method of animal class......")

class Human:
    def __init__(self):
        print("Human Ctor.....")

    def talk(self):
        print("Humans talk......")

    def fun(self):
        print("fun method of human class.....")

class Girl(Animal, Human):

    def __init__(self):
        super().__init__()
        Human.__init__(self)
        print("Girl Ctor......")

    def read(self):
        print("girls can read.....")

tina = Girl()
tina.eat()
tina.talk()
tina.read()
tina.fun()