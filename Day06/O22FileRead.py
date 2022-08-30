
FL = open("data.txt", "r")

# st = FL.read()

# st = FL.readline(200)                  # reads one line (one paragraph)

st = FL.readlines(900)                      # reads all lines and store it like a list
print(st)

# for line in st:
#     print(line)

FL.close()