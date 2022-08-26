
d1 = [(x, y) for x in range(3) for y in range(3)]
print(f"d1 :{d1}")
print("-" * 40)

d2= [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(f"d2 :{d2}")
print("-" * 40)

d3 = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]
print(f"d3 :{d3}")
print("-" * 40)

players = {
    'sachin': [300, 345, 225, 205, 285],
    'sourav': [200, 305, 330, 405, 150],
    'rahul': [145, 230, 298, 360, 215],
    'sehwag': [120, 150, 405, 380, 450],
    'yuvraj': [185, 205, 230, 120, 160],
    'laxman': [105, 185, 250, 385, 180]
}

print(f"players :{players}")
print("-" * 40)

print(f"sachin :{players['sachin']}")
print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)
plyr_score = {k: sum(v) for k, v in players.items()}
print(f"plyr_score :{plyr_score}")

print("-" * 40)
plyr_score = {k: (lambda scores: sum(scores) / len(scores))(v)
              for k, v in players.items()}
print(f"plyr_score :{plyr_score}")

print("-" * 40)
def avg_scr(runs):
    return sum(runs) / len(runs)

plyr_score = {k: avg_scr(v) for k, v in players.items()}
print(f"plyr_score :{plyr_score}")

print("-" * 40)
basic1 = [{x: (lambda par: "Mr." + par)('Sachin {}'.format(x))}
          for x in range(1, 6)]
print(f"basic1 :{basic1}")


print("-" * 40)
vals = {(lambda par: par * 10)(k): (lambda par : par * par)(v)
        for k, v in {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}.items()}
print(f"vals :{vals}")

print("-" * 40)
plyr_score = [score for score in players.values()]
print(f"plyr_score :{plyr_score}")

print("-" * 40)
plyr_score = [x for score in players.values() for x in score]
print(f"plyr_score :{plyr_score}")

print("-" * 40)
plyr_score = [x for score in players.values() for x in score if x >= 200]
print(f"plyr_score :{plyr_score}")

players = {
    'sachin': [300, 345, 225, 205, 285],
    'sourav': [200, 305, 330, 405, 150],
    'rahul': [145, 230, 298, 360, 215],
    'sehwag': [120, 150, 405, 380, 450],
    'yuvraj': [185, 205, 230, 120, 160],
    'laxman': [105, 185, 250, 385, 180]
}
print("-" * 40)

"""
sachin : [>=200]
plyr_score = [x for score in players.values() for x in score if x >= 200]
"""

plyr_score = {name: [scr for scr in score if scr >= 200] for name, score in players.items()}
print(f"plyr_score :{plyr_score}")