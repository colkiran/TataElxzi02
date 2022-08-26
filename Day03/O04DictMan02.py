
print("keys".center(40, "-"))

player = {'name': 'Tendulkar', 'runs': 210, 'oppn': 'Ban', 'venue': 'Eden Garden', 'age': 39, 'year': 2014}

k = player.keys()
print(f"k :{k}")
print(type(k))

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Tendulkar', 'runs': 210, 'oppn': 'Ban', 'venue': 'Eden Garden', 'age': 39, 'year': 2014}

print(f"player :{player}")
v = player.values()
print(f"values :{v}")

print("setdefault".center(40, "-"))
# add new key value pairs to the dictionary

player = {'name': 'Tendulkar', 'runs': 210, 'oppn': 'Ban', 'venue': 'Eden Garden', 'age': 39, 'year': 2014}
print(f"player :{player}")
player.setdefault("gender", "Male")
player.setdefault("Team", "India")
player.setdefault("name", "Sachin")
player.setdefault("oppn", "SA")

print(f"player :{player}")

print("fromkeys".center(40, "-"))
# convert a list into a dictionary, elements of the list will become keys

cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 25)
print(f"res2 :{res2}")

print("pop".center(40, "-"))

player = {'name': 'Tendulkar', 'runs': 210, 'oppn': 'Ban', 'venue': 'Eden Garden', 'age': 39, 'year': 2014}
print(f"player :{player}")

res = player.pop("runs")
print(f"player :{player}")
print(f"res :{res}")

# res = player.pop("runs")
# print(f"player :{player}")
# print(f"res :{res}")

print("popitem".center(40, "-"))

player = {'name': 'Tendulkar', 'runs': 210, 'oppn': 'Ban', 'venue': 'Eden Garden', 'age': 39, 'year': 2014}
print(f"player :{player}")

# player = {}
res = player.popitem()
print(f"player :{player}")
print(f"res :{res}")

res = player.popitem()
print(f"player :{player}")
print(f"res :{res}")

