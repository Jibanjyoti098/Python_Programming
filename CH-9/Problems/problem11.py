with open("CH-9/Problems/new.txt") as f:
    c = f.read()

with open("CH-9/Problems/new_copy.txt", "w") as f:
    c = f.write(c)

with open("CH-9/Problems/rename_new_copy.txt", "w") as f:
    c = f.write(str(c))
    