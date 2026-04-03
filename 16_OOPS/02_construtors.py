class Employee:
    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond

    def get_salary(self):
        pass
    def get_info(self):
        print(f"the name of employee is {self.name}. his salary is {self.salary}. the bond is for {self.bond}years")


e1=Employee(34000, "tung tung sahur",4)
print(e1.get_salary())
e1.get_info()
        