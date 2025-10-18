class Employee:

    def __init__(self, nam, salary, language):
        self.name = nam
        self.salary = salary
        self.language = language



jiban = Employee("Jiban", 12000, "Py")
print(jiban.name, jiban.salary, jiban.language)