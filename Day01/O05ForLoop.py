
for i in range(5):
    print("Hello World")

print("-" * 40)

for i in range(1, 6):
    print(f"{i}. Hello World")

print("-" * 40)
for i in range(1, 6, 1):            # start from 1, go upto value <6, incr by 1
    for j in range(1, i+1):
        print(j, end="")
    print("")


print("-" * 40)
# continue, break, else
for i in range(1, 25):
    # if i > 20:
    #     break
    if i % 2 == 0:
        continue
    print(i, end=" ")
else:
    print("\niteration completed....")
print("")
