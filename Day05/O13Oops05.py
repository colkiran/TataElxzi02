
class Player:
    Plyr_Cntr = 0
    Team = "India"

    def __init__(self, name, age):                         # constructor
        self.name = name
        self.age = age
        Player.Plyr_Cntr += 1

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")
        print(f"There are {Player.Plyr_Cntr} players")

ply1 = Player("Sachin", 39)
ply1.get_details()
print("-" * 40)
ply2 = Player("Sourav", 38)
ply2.get_details()
print("-" * 40)
ply3 = Player("Rahul", 36)
ply3.get_details()
print("-" * 40)


print("-" * 40)
ply3.get_details()
print("-" * 40)
ply2.get_details()
print("-" * 40)
ply1.get_details()

print("-" * 40)
print("-" * 40)

print(f"Player :{Player.Team}")
print(f"ply1 :{ply1.Team}")
print(f"ply2 :{ply2.Team}")
print("-" * 40)

Player.Team = "MI"
print(f"Player :{Player.Team}")
print(f"ply1 :{ply1.Team}")
print(f"ply2 :{ply2.Team}")

print("-" * 40)
ply2.Team = "RCB"
print(f"ply2   :{ply2.Team}")
print(f"Player :{Player.Team}")
print(f"ply1   :{ply1.Team}")

print("-" * 40)
print(ply2.__dict__)

print("-" * 40)
print(Player.__dict__)
