
st = "Hello World"
print(f"st :{st}")
print(type(st))

print("-" * 40)
print(st[0])                # strings are stored like lists
print(st[6])
print(st[10])

# slicing
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")


print("-" * 40)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 40)
# slicing reverse
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")


print("-" * 40)
# st=input("enter a name:")
st = 'abba'
if(st[:]==st[::-1]):
    print("palindrome")
else:
    print("not a palindrome")

print("-" * 40)
# strings are immutable
st = "Hello World"
print(f"st :{st}")
print(f"st[6] :{st[6]}")
# st[6] = "w"

print("-" * 40)
st = "hello world"
st1 = "the quick brown fox jumps over the lazy dog"

print(f"st :{st}")
print(f"st1 :{st1}")

# find -  will return the index of the character or word if found else returns -1
pos = st.find('l')
print(f"pos :{pos}")

print("pos :", st.find("l", st.find("l", st.find("l") + 1)+1))

pos = st1.find("the")
print(f"pos :{pos}")

pos = st1.find("the", st1.find("the") + len("the"))
print(f"pos :{pos}")

print("-" * 40)
print(dir(st))