
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)
for lt in letters:
    print(lt, end= " ")
print()

for letter in enumerate(letters):
    print(letter," ", end="" )
print()

for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 40)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mylist)

print("-" * 40)
for lst in mylist:
    print(lst)

print("-" * 40)
for idx, lst in enumerate(mylist):
    print(f"List({idx})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")


print("-" * 40)
print(dir(mylist))
