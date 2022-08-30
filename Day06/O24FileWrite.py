"""
if the file exists then
       1. deletes the content of the file
       2. write newly into the file
"""

FL = open("myfile.txt", "w")

# st = input("Enter the content of the file :")
# FL.write(st)

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"

FL.writelines([l1, l2, l3])

FL.close()

print("-" * 40)

ch = "y"
st = ""
while ch == "y":
    st += input("Enter the content of the file :") + "\n"
    print(st)
    ch = input("Do you want to continue (y/n)?")

FW = open("result.txt", "w")
FW.write(st)
FW.close()