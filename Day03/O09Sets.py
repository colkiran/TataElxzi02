
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 40)

s2 = {1, 2, 3, 'four', 'five', 'six', 7.2, 8.9, 9.0, True, False, 10+0J, 11-2j}
print(f"s2 :{s2}")
print(type(s2))
print("-" * 40)

s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))
print("-" * 40)

s4 = {1, 2, 3}
print(f"s4 :{s4}")

# add elements into a set -> add, update
s4.add(2)
s4.add(1)
s4.add(4)
s4.add(3)
s4.add(5)
s4.add(6)
print(f"s4 :{s4}")

s4.update([1, 2, 3])
s4.update([3, 4, 5])
s4.update([5, 6, 7])
s4.update([4, 5, 6])
s4.update([8, 9, 10])

print(f"s4 :{s4}")

print("-" * 40)
# delete values of a set -> pop, remove, discard
res = s4.pop()
print(f"s4 :{s4}")
print(f"res :{res}")

res = s4.pop()
print(f"s4 :{s4}")
print(f"res :{res}")

s4.remove(8)
s4.remove(4)
# s4.remove(1)
print(f"s4 :{s4}")

s4.discard(7)
s4.discard(5)
s4.discard(1)
print(f"s4 :{s4}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}
print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print("A union B :", A | B)
print("B Union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric_difference B :", A ^ B)
print("B symmetric_difference A :", B.symmetric_difference(A))

# frozen_set - immutable
fs1 = frozenset([1, 2, 3, 4, 5])
print(f"fs1 :{fs1}")
print(type(fs1))