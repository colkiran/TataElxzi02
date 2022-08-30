
def Calc(fnc):
    loginfo = "Logging into the service......"

    def innerFun(a, b):
        print(loginfo)
        if b > a:
            a, b = b, a
        print(fnc(a, b))                # call back
        print("-" * 40)

    return innerFun