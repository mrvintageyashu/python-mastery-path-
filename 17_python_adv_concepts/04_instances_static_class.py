class Employee:
    company= "MR.Vintage"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    #instances methods default
    def print_info(self):
        info = f"the name is {self.name} and the salary is the {self.salary}"
        print(info)
    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

e1=Employee("sujal",100000)
e2=Employee("haris",1233123)
#print(Employee.company)
#e1.print_info()
#e2.print_info()
#print(e2.sum(4,22))
e1.print_company()
e1.change_company("MR.Yintage")
e1.print_company()
print(Employee.company)