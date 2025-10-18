with open("CH-9/Problems/word.txt") as f:
    c = f.read()
with open("CH-9/Problems/word_copy.txt", "w") as f:
    f.write(c)