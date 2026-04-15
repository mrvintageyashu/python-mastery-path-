class Employee:
    company="yintage"
    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        pass
    def get_info(self):
        print(f"the name of employee is {self.name}. his salary is {self.salary}. the bond is for {self.bond}years")

e1=Employee(3400,"ridhi",9,"google")
print(e1.company)
print(Employee.company)
print(dir(e1))
