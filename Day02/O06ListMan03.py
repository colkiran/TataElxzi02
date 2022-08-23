

print("{:*^40}".format("append"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
print(type(l1))

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

arr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
arr[0][0] = 1
arr[1][1] = 1
arr[2][2] = 1

print("-" * 40)
for ar in arr:
    print(ar)

print("{:#^40}".format("insert"))

l2 = list(range(1, 6))
print(f"l2 :{l2}")

l2.insert(1, 1.5)
l2.insert(3, 2.5)
l2.insert(5, 3.5)
l2.insert(7, 4.5)

print(f"l2 :{l2}")

print("{:@^40}".format(" APPEND "))

l3 = list(range(2, 15, 2))
print(f"l3 :{l3}")

l3.extend([16, 18, 20])
l3.extend([22, 24, 26])

print(f"l3 :{l3}")

print("pop".center(40, "-"))

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(3)
print(f"l1 :{l1}")
print(f"res :{res}")

res = l1.pop(8)
print(f"l1 :{l1}")
print(f"res :{res}")

res = l1.pop()                              # removes the last element from the list
print(f"l1 :{l1}")
print(f"res :{res}")

print("remove".center(40, "="))
l2 = [1, 2, 3, 1, 2, 1, 2, 1, 1 ,1 ,1, 1, 1, 2, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1 ,1, 1, 3]
print(f"l2 :{l2}")

rs = l2.remove(1)
print(f"l2 :{l2}")
print(f"rs :{rs}")

l2.remove(3)
print(f"l2 :{l2}")

# while True:
#     try:
#         l1.remove(1)
#     except ValueError:
#         break


while l1.count(1):
    l1.remove(1)

print(f"l1 :{l1}")