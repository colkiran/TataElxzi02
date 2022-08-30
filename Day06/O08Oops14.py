
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("getter called.....")
        return self.__price

    def set_price(self, val):
        print("setter called.....")
        if val < 0:
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = val

    def del_price(self):
        print("deleter called....")
        self.__price = 0

    price = property(get_price, set_price, del_price)

pepsi = Product(45)
print(pepsi.price)
pepsi.price = 75
print(pepsi.price)
del pepsi.price
print(pepsi.price)



