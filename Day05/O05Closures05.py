
def fun1():
    return("fun1 has no args....")

def fun2(x):
    return(f"fun1 has one args....:{x}")

def fun3(x, y):
    return(f"fun1 has two args.... :{x}, {y}")

def fun4(x, y, z):
    return(f"fun1 has no args.... :{x}, {y}, {z}")

def log_Details(fnc):
    loginfo = "Logging into the system....."

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

infun = log_Details(fun1)
infun()
print("*" * 40)

infun = log_Details(fun2)
infun(10)
print("*" * 40)

infun = log_Details(fun3)
infun(100, 200)
print("*" * 40)

infun = log_Details(fun4)
infun(5, 10, 15)
print("*" * 40)


