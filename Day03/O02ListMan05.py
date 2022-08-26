
lst1 = [10, 5, 8, 1, 9, 2, 4, 6, 3, 7]
print(f"lst1 before :{lst1}")

asc_res = sorted(lst1)
print(f"asc_res :{asc_res}")
desc_res = sorted(lst1, reverse=True)
print(f"desc_res :{desc_res}")

lst1.sort()
print(f"lst1 :{lst1}")

print("-" * 40)
lst2 = [10, 'zebra', 'apple', 5, 'yellow', 'blue', 8, 'violet', 'green', 1, 'pink', 'red', 9, 'dog', 'hen', 2, 'orange', 'magenta', 4, 'white', 'cat', 6, 3, 7, 19, 185, 1234, 27, 234, 2067, 38, 398, 3451]

print(f"lst2 before :{lst2}")
asc_res1 = sorted(lst2, key=ascii)
print("\n")
print(f"Ascending :{asc_res1}")

print("-" * 40)
lst3 = ['thiruvananthapuram', 'bangalore', 'kanyakumari', 'delhi', 'ooty', 'hyderabad', 'chennai', 'mumbai', 'pune', 'vishakapatnam', 'mysore']
print(f"lst3 :{lst3}")
print("\n")
res = sorted(lst3, key=len)
print(f"res :{res}")

print("-" * 40)

months = ['dec', 'apr', 'aug', 'nov', 'feb', 'sep', 'mar', 'may', 'jul', 'jun', 'jan', 'oct']
print(f"months :{months}")
from calendar import month_name
# print(f"month_name :{month_name}")
# print(f"month_name :{list(month_name)}")

def sortMth(mon):
    l = []
    for m in list(month_name):
        l.append(m[0:3].lower())
    if mon in l:
        return l.index(mon)

sortedMonths = sorted(months, key=sortMth)
print("\n")
print(f"Sorted Months :{sortedMonths}")

print("{:*^40}".format("reverse"))
lst1 = [10, 5, 8, 1, 9, 2, 4, 6, 3, 7]
print(f"lst1 :{lst1}")
print(list(reversed(lst1)))
