letter = '''Dear<|Name|>,\nYou are selected!\n<Date> '''
print(letter.replace("<|Name|>", "Jiban").replace("<Date>", "17 june 2025"))
# replaced a string through chaining replace