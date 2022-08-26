
lst1 = list(range(10, 101, 10))
print(f"lst1 before :{lst1}")

lst1.clear()
print(f"lst1 after :{lst1}")

print("{:-^40}".format("Count"))
lst2 = [1, 2, 3, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 3 ,4, 1, 2, 3, 2, 1, 2, 1, 2, 2, 3, 1, 1, 2, 1]

print(f"lst2: {lst2}")
print(f"1 :{lst2.count(1)}")
print(f"2 :{lst2.count(2)}")
print(f"3 :{lst2.count(3)}")
print(f"8 :{lst2.count(8)}")

print("index".center(40, "-"))
print(f"lst2 :{lst2}")
print(f"lst2.index(3) :{lst2.index(3)}")
print(f"lst2.index(3) :{lst2.index(3, lst2.index(3) + 1)}")
print(f"lst2.index(3) :{lst2.index(3, lst2.index(3, lst2.index(3) + 1) + 1)}")

print("copy".center(40, "-"))
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 before :{lst1}")
lst2 = lst1                             # shallow copy (data + address)
print(f"lst1 :{id(lst1)} \t lst2 :{id(lst2)}")
print(f"lst2 before :{lst2}")

print("-" * 40)
lst2.extend([6, 7, 8, 9])
print(f"lst2 after :{lst2}")
print(f"lst2 after :{lst1}")
 
print("=" * 40)
lst3 = [10, 20, 30, 40, 50]
print(f"lst3 before :{lst3}")
lst4 = lst3.copy()                      # deep copy (data shared)
print(f"lst4 before :{lst4}")

print("-" * 40)
lst4.insert(1, 15)
lst4.insert(3, 25)
lst4.insert(5, 35)
print(f"lst4 after :{lst4}")
print(f"lst3 after :{lst3}")

print("=" * 40)
lst5 = [11, 22, 33, 44, [45, 46, 47, 48] ,55]
print(f"lst5  before:{lst5}")
lst6 = lst5.copy()
print(f"lst6 before :{lst6}")

print("-" * 40)
lst6[4].append(49)
lst6[4].append(50)
lst6[4].append(51)

print(f"lst6 after :{lst6}")
print(f"lst5 after :{lst5}")

print("=" * 40)
lst7 = [2, 4, 6, [1, 2, 3, 4, 5], 8, 10]
print(f"lst7 before :{lst7}")
from copy import deepcopy

lst8 = deepcopy(lst7)
print(f"lst8 before :{lst8}")

print("-" * 40)
lst8[3].extend([6, 7, 8])
print(f"lst8 after :{lst8}")
print(f"lst7 after :{lst7}")