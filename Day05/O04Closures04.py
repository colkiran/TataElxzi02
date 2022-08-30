
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun
    return innerFun

kanGrt = outerFun("Namaskara")
tgrGrt = kanGrt("lion")
tgrGrt("Prabhakar")

"""
outerFun("Welcome")("----->")("Sachin")
print("-" * 40)

engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")

engSarw = engGrt("----->")
engDawr = engGrt("=====>")
tmlSarw = tmlGrt("----->")
tmlHarw = tmlGrt("#####>>")

engSarw("Rahul")
tmlSarw("Dhoni")
"""