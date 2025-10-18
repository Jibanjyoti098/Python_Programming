class Employee:
    language = "Py"
    salary = 12000 #class attribute

jiban = Employee()
jiban.name = "JIBAN" #object attribute
print(jiban.name, jiban.language)

risi = Employee()
risi.name = "RISI"
print(risi.language, risi.name)