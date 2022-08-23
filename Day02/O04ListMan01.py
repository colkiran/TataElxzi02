
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9.5, 10.2, 11.8, 12.1, True, False,
      15+0j, 30+2j]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(3, 25, 3))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l1 = [1, 2, 3, 4.5, 5.7, 6.2]
print(f"l1 :{l1}")

print(f"id(l1[0] :{id(l1[0])}")
print(f"id(l1[1] :{id(l1[1])}")
print(f"id(l1[2] :{id(l1[2])}")
print(f"id(l1[3] :{id(l1[3])}")

print("-" * 40)
# creation and updation
l1 = list(range(1, 11))
print(f"l1 :{l1}")
l1[5] = 66
print(f"l1 :{l1}")

# read
print(f"l1[3] :{l1[3]}")
for i in l1:                            # iterating through a list
    print(i, end=" ")
print()

# delete
del l1[2]
del l1[5]
del l1[7]
print(f"l1 :{l1}")

print("-" * 40)
values = list(range(10, 40, 10))
print(f"values  :{values}")

a, b, c = values                  # unpack
print(a, b, c)

print("-" * 40)
values = list(range(10, 101, 10))
print(f'values :{values}')
a, b, *c = values
print(a, b, c)
a, *b, c = values
print(a, b, c)
*a, b, c = values
print(a, b, c)

print("-" * 40)
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

l3 = [lst1, lst2]
print(f"l3 :{l3}")
print("l3  :{len(l3)}")

print("-" * 40)
l5 = [*lst1, *lst2]             # unpack the list and the store it
print(len(l5))

