
def add(x, y):
    return x + y

a = add
res = a(10, 20)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y: x + y
res = b(45, 35)
print(f"res :{res}")

print("-" * 40)
# map, filter and reduce

print("map".center(40, "-"))
l = list(range(1, 11))

squares = list(map(lambda x : x ** 2, l))
print(squares)

cel = [23, 28, 30, 32, 36, 40, 42, 45, 50]
# convert this into farenhiet
# c * 1.8  + 32
print("-" * 40)

months = ['dec', 'apr', 'aug', 'nov', 'feb', 'sep', 'mar', 'may', 'jul', 'jun', 'jan', 'oct']

print(f"Unsorted Months :{months}")
from calendar import month_name
# print(list(month_name))

sorted_months = sorted(months, key=list(map(lambda x: x.lower()[0:3], list(month_name))).index)

print(f"sorted months :{sorted_months}")

# Filters
print("filters".center(40, "-"))
l = list(range(1, 26))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("reduce".center(40, "-"))
from functools import  reduce
l = list(range(1, 11))
print(f"l :{l}")
res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")

print("-" * 40)
l = [10, 7, 4, 6, 9, 11, 5, 3, 8, 12]

top = reduce(lambda x, y: x if x > y else y, l)
print(f"top :{top}")
