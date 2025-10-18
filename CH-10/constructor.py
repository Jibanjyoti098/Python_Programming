class Employee:
    language = "Py"
    salary = 12000 #class attribute

    def __init__(self, name, salary, language):#dunder method, automatically called
        print("I am creating an object")
        self.name  = name
        self.salary  = salary
        self.language = language

    @staticmethod
    def greet():
        print("Good morning")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


jiban = Employee("Jiban", 15500, "java")
# jiban.language = "java" #object attribute
print(jiban.salary, jiban.language, jiban.name)
# jiban.getInfo()
# Employee.getInfo(jiban)