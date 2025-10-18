class Employee:
    language = "Py"
    salary = 12000 #class attribute

jiban = Employee()
jiban.language = "Java" #object attribute
print(jiban.salary, jiban.language)
