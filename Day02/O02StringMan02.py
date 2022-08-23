
st = "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

print(f"st :{st}")
print(f"st1 :{st1}")

print("replace".center(40, "-"))
res = st.replace("w", "W")
print(f"res :{res}")
res1 = res.replace("h", "H")
print(f"res1 :{res1}")

res2 = st.replace("l", "L")
print(f"res2 :{res2}")

res2 = st.replace("l", "L", 2)
print(f"res2 :{res2}")

res = st1.replace("the", "The")
print(f"res :{res}")

res = st1.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 40)
print(dir(st1))

print("Maketrans".center(40, "-"))
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"

# length of a and b should be the same
trans_tbl = st.maketrans(a, b)
print(trans_tbl)

res = st.translate(trans_tbl)
print(f"res :{res}")

print("-" * 40)
st = "Raju has secured {n} marks in his 10th"
print(f"st :{st}")
print(st.format(n=75))
