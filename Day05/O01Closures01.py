
def outerFun(gname):
    info = f"Mr. {gname}"

    def innerFun():
        nonlocal info
        print("Hello World")
        info = info + " Tendulkar"
        print(f"Greeting {info}")

    innerFun()


outerFun("Sachin")