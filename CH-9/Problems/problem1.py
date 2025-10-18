f = open("CH-9/Problems/poem.txt")
c = f.read()
if("twinkle" in c):
    print("It is is the content")
else:
    print("Not present in the content.")
f.close()