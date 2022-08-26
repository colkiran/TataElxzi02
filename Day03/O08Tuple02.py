
from collections import namedtuple

nmdTpl = namedtuple("Product", "prodid pname price catg")
prod = nmdTpl(prodid="P101", pname="Dairy Milk", price=175, catg='Choclate')
print(prod)
print("-" * 40)

print(f"prodid    :{prod.prodid}")
print(f"prod_Name :{prod.pname}")
print(f"Price     :{prod.price}")
print(f"Category  :{prod.catg}")

# prod.price = 200