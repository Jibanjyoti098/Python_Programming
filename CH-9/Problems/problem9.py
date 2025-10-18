with open("CH-9/Problems/word.txt") as f:
    c1 = f.read()

with open("CH-9/Problems/word_copy.txt") as f:
    c2 = f.read()

if(c1==c2):
    print("These are identical files")
else:
    print("These are not identical files")
