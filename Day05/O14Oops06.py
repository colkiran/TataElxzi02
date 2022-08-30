
class Player:
    Plyr_Cntr = 0
    Team = "India"

    def __init__(self, name, age):                         # constructor
        print("Player Ctor......")
        self.name = name
        self.age = age
        Player.Plyr_Cntr += 1

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")
        print(f"There are {Player.Plyr_Cntr} players")

    @classmethod
    def Change_attr(cls, tm_name):
        cls.Team = tm_name

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("factory....")
        return cls(f"{fname} {lname}", age)                 # calls the constructor


ply1 = Player("Tyson", 45)
ply1.get_details()
Player.Change_attr("Sahara India")
print(Player.Team)

print("-" * 40)
ply2 = Player.CreatePlayer("Mike", "Tyson", 46)
ply2.get_details()
