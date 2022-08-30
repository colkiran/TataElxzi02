
import mypackage.Mymodule as m
from mypackage.Mymodule import Product

m.greet("Rahul")
print(m.sports)
print(m.runs)

print("-" * 40)
p1 = Product("lays", 20)
p2 = Product("pringles", 120)

p1.get_details()
p2.get_details()