
def greet():
    print("Greeting Mr.Sachin, Welcome to the event, Pleasure to dine with you....")

def greetGst(gname):
    print(f"Greeting Mr.{gname}, Welcome to the event.....")

# city is a default argument and name is a non default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greeting Mr.{gname} from {city}, Welcome to the event.....")


greet()
greetGst("Rahul")
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", city="Bangalore")

print("-" * 40)

def admission(fname, lname, dob, qlf, gender, ctcno, adr, city):
    print(f"Name is         :{fname} {lname}")
    print(f"DOB is          :{dob}")
    print(f"Qualification   :{qlf}")
    print(f"Gender          :{gender}")
    print(f"Contact No.     :{ctcno}")
    print(f"Address         :{adr}")
    print(f"City            :{city}")

# *args       - pass the arguments like a list      -   ('mike', 'tyson'....)
# **kwargs    - pass the arguments like a dictionary    -   (fname='mike',
#                                                                     lname='tyson')
admission(ctcno="9834923940", dob="04/05/1983", qlf="B.E", city="Delhi", fname='Mike', lname='Tyson', gender="Male", adr="MG Road, New Delhi")

print("-" * 40)
# function return values
def MultiplyMe(x, y):           # called function
    print(x * y)
    return x * y
    print("Hello World")


res = MultiplyMe(4, 5)          # calling function

print(f"The product of 4 and 5 is :{MultiplyMe(4, 5)}")

print("-" * 40)

def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x - 1)

print(f"The factorial of 5 is :{fact(5)}")

def fiba(iter):
    if iter <= 1:
        return iter
    else:
        return fiba(iter - 1) + fiba(iter  - 2)

# itrs = int(input("Enter the number of iterations :"))
itrs = 5
print(f"fibanocii Series")
for i in range(itrs):
    print(fiba(i), end= " ")
print()


print("-" * 40)

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 40)
# Varaible Length Argument
def Calcprod(*numbers):                     # can accept more than one value
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = Calcprod(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)
def extractDetials(**details):
    # print(details)
    for i in details:
        print(i, "=>", details[i])

extractDetials(name="sachin", runs=150, oppn="Aus", vunue="Perth")

print("-" * 40)
# Doc Strings

def fun():
    # this is a comment
    "This a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("=" * 40)

def fun1(x, y):
    """
        Function fun1
        -------------
        res = fun1(x, y)

        if x and y are integers then fun1 returns the sum of x and y
        if x and y are strings the fun1 returns the concatenation of x and y

    """
    return x + y

print(fun1(35, 55))
print(fun1("hello", "world"))
# print(fun1.__doc__)

print("-" * 40)
print("-" * 40)
help(fun1)
