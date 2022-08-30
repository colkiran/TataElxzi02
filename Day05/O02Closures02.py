
def outerFun(gname):                # HOF  - Higher Order Functions
    info = f"Mr. {gname}"

    def innerFun():
        nonlocal info
        print("Hello World")
        info = info + " Tendulkar"
        print(f"Greeting {info}")

    return innerFun


outerFun("Sachin")()
print("-" * 40)

infun = outerFun("Sachin")

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

print("-" * 40)
infun()                                 # calls the innerFun