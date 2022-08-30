
class Player:                           # pascal casing

    def get_runs(self):                 # self is reffering an object
        print("Runs scored......")

sachin = Player()                       # sachin is an object of the Player class
sachin.get_runs()                       # implicitly pass arguments to get_runs

print("-" * 40)
print(type(sachin))


print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
