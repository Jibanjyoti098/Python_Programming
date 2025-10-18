word = "Donkey"

with open("CH-9/Problems/word.txt", "r") as f:
    content=f.read()
contentNew = content.replace(word, "#####")
with open("CH-9/Problems/word.txt", "w") as f:
    f.write(contentNew)