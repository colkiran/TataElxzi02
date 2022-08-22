x = 0
for i  in range (50,150):
    count = 0
    for j in range (1,i+1):
        if i%j == 0:
           count += 1
        if count > 2:
           break
    else:
        print (i, end =" ")
        x += 1
print (f"\nthe number of prime numbers are {x}")
