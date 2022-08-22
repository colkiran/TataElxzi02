
"""
1. Arithmetic
2. Comparison or relational
3. logical
4. Bitwise
5. Ternary
"""

print("Arithmetic Operators".center(40, "-"))
print(f"10 + 3  = {10 + 3}")
print(f"10 - 3  = {10 - 3}")
print(f"10 * 3  = {10 * 3}")
print(f"10 / 3  = {10 / 3}")
print(f"10 // 3  = {10 // 3}")              # floor division
print(f"10 % 3 = {10 % 3}")                 # modulus
print(f"10 ** 3 = {10 ** 3}")

print("Augmentor".center(30,"-"))
# =, +=, -=, /=, *=
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x /= 3
print(f"x :{x}")

print("Comparison Operators".center(40, "-"))
# ==, >=, <=, <, >, !=

a = 10
b = 15
print(f"a,b :{a, b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"b >= a :{b >= a}")
print(f"a <= b :{a <= b}")

print("logical Operators".center(40, "-"))
print(1 == 1 and 2 == 2)
print(1 == 1 and 1 == 2)
# or

print(1 == 1 or 1 == 2)
print(1 == 2 or 2 == 1)

#not
print(not(1 == 1 or 1 == 2))
print(not(1 == 2 or 2 == 1))

print("-" * 40)
print(f"ord('a') :{ord('a')}")              # integer representation of unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(40, "-"))

print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)

print(5 >> 1)
print(16 >> 1)
print(~0)
print(~5)

# ternary Operator
print("-" * 40)
a = 10
print('Eligible' if a >= 18 else "Not Eligible")