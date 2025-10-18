def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["Jiban", "Risi", "Biswajeet", "Rajesh", "R"]
# element = input("Enter element to remove: ")
print(rem(l, "R"))