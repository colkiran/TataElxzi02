
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'sachin', 'runs': 125, 'oppn': 'Aus', 'venue': 'Gabba'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sourav'), ('run', 97), ('oppn', 'West Indie'), ('venue', 'Sabina Park' )])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="sachin", age="25", runs=85, oopn= "newzealand", venue="auckland" )
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'Sachin', 'runs': '210', 'oppn': 'Ban', 'venue': 'Eden Garden'}
print(f"player :{player}")

print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
player['age'] = 39
player['year'] = 2014
player['name'] = "Tendulkar"
print(f"player :{player}")

# iterate through the dictionary
for x in player:
    # print(x, end=" ")
    print(x, "=>", player[x])
print()

del player['age']
print(player)

print("-" * 40)
print(player.get('name'))
print(player.get('gender', "Please enter a valid key"))

print("-" * 40)
print(dir(player))