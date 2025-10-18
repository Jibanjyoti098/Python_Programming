class Programmer:
    company = "IPSAR"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin



p = Programmer("Jiban", 12000, 754153)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("risi", 12000, 754155)
print(r.name, r.salary, r.pin, r.company)