

def timeCalc(fnc):

    def innerFun(val):
        from datetime import datetime
        st = datetime.now()
        fnc(val)
        et = datetime.now()
        print(f"The Total Time taken by {fnc.__name__} is {et - st}")
    return innerFun


@timeCalc
def fun(max):
    l = []
    for i in range(1, max):
        for j in range(1, i + 1):
            l.append(j ** 2)

fun(5000)
