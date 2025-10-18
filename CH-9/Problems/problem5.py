words = ["Donkey", "bad", "Ganda"]

with open("CH-9/Problems/word.txt", "r") as f:
    content=f.read()
    
for word in words:
    content = content.replace(word, "#"*len(word))
        
with open("CH-9/Problems/word.txt", "w") as f:
    f.write(content)