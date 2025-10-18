f = open("CH-9/file.txt")

# # lines = f.readlines()
# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))
# f.close()
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close() 