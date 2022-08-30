
gname = "Sachin"

sports = ['cricket', 'soccer', 'tennis', 'hockey', 'swimming']

runs = {'tests': 18500, 'ODI': 15200, 'T20': 2500}

def greet(gst):
    print(f"Greeting {gst}, Welcome to the annual meet......")

class Product:

    prdCntr = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.prdCntr += 1

    def get_details(self):
        print(f"Name is {self.name}\nPrice is {self.price}")
        print(f"There are {Product.prdCntr} products added....")

print(f"Module :{__name__}")

if __name__ == '__main__':
    kitkat = Product("KitKat", 40)
    kitkat.get_details()

