
class Animal:

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly......")

class Chicken(Bird):

    def Msg(self):
        print("Chicken's are breeded for consumption......")

    def fly(self):              # overriding parent class property.....
        print("Chickens seldom fly.....")

chic = Chicken()
chic.eat()
chic.fly()
chic.Msg()
