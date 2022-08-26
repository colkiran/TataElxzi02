
def OuterFun():
    gname = "Sachin"                # local variable

    # only local variable can be converted into non-local variable (global can't)
    def InnerFun():
        nonlocal gname
        gname = "Mr." + gname
        print(f"Hello {gname}")

    InnerFun()
    print(f"Outerfun :{gname}")


OuterFun()