marks = {
    "Jiban": 100,
    "Risi": 34,
    "Biswajeet": 45
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Jiban": 99, "Chandan": "Fail"})
print(marks)
print(marks.get("Harry"))#It will show none
# print(marks["Harry"])#If doesn't exist it will show error
print(len(marks))
