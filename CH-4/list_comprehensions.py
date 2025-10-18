squares = [x**2 for x in range (5)]
print(squares)#0-4 square of each

even_number = [x for x in range(10) if x%2==0]
print(even_number)

matrix = [[row * col for col in range(3)] for row in range(4)]
print(matrix)

fruits = ["apple", "orange", "grapes"]
for fruit in fruits:
    print(f"I'll take {fruit}")