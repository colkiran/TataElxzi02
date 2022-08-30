
def callMe():
    print("Apples from Ooty.......")

def fun(fnc):
    print("Hello.....")
    fnc()           # call back
    print("Hi......")
    print("-" * 40)

    def defineMe():
        print("Oranges from kanpur....")

    return defineMe

def FuncallBack(fnc):
    print("Mera Bharath Mahan......")
    fnc()
    print("India is Great.........")

FuncallBack(fun(callMe))




