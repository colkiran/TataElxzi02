
import Mymodule as m
from Mymodule import Product

m.greet("Rahul")
print(m.sports)
print(m.runs)

print("-" * 40)
p1 = Product("Dairy Milk", 80)
p2 = Product("5 Star", 20)

p1.get_details()
p2.get_details()