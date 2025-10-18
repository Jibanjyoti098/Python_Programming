class Employee:
    language = "Py"
    salary = 12000 #class attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


jiban = Employee()
jiban.language = "java" #object attribute
print(jiban.name, jiban.language)
jiban.getInfo()
Employee.getInfo(jiban)