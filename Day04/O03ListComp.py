
l1 = [x ** 2 for x in range(1, 11)]                 # list comprehension
print(f"l1 :{l1}")

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"Sentence :{sentence}")

print("-" * 40)
words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 40)
words = [(word, len(word)) for word in sentence.split()]
print(f"words :{words}")

print("-" * 40)
words = [(word, len(word)) for word in sentence.split() if word != "the"]
print(f"words :{words}")

print("-" * 40)
print("-" * 40)

fruits = [
    ('apple', 285),
    ('orange', 145),
    ('grapes', 120),
    ('banana', 65),
    ('pine', 80),
    ('gauva', 90),
    ('strawberry', 350),
    ('water melon', 75)
]

print(f"fruits :{fruits}")

print("-" * 40)
price = ["fruits" for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
price = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits]
print(f"price :{price}")

print("-" * 40)
expFrts = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] >= 100]

print(f"price :{price}")
