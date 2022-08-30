
def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun


engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

# simple curry
engGrt("Messi")
hndGrt("Jadeja")
tmlGrt("Natrajan")