import os

# List entries in the current directory
entries = os.listdir()
print(entries)

# List entries in a specific directory
path = '/'
entries = os.listdir(path)
print(entries)
