
import gurgaon.Mymodule as m
from gurgaon.Mymodule import Product

m.greet("Rahul")
print(m.sports)
print(m.runs)

print("-" * 40)
p1 = Product("kurkure", 20)
p2 = Product("haldirams", 120)

p1.get_details()
p2.get_details()