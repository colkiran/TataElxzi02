
def diff(x,y):
    return f"The difference of {x} and {y} is :{x - y}"


def outerFun(fnc):
    loginfo = "Logging into the service......"

    def innerFun(a, b):
        print(loginfo)
        if b > a:
            a, b = b, a
        print(fnc(a, b))                # call back
        print("-" * 40)

    return innerFun


infun = outerFun(diff)
infun(10, 25)
