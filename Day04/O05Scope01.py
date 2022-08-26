
glbX = 100

def fun(a):                 # local variable
    global glbX             # do not assign any value in this line
    print(f"a :{a}")
    glbX = 500 
    print(f"Inside :{glbX}")
    b = "Hello"             # local Variable
    print(f"b :{b}")

print(f"Before :{glbX}")

fun(25)

print(f"After :{glbX}")
