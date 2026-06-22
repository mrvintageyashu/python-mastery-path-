class MathUtils:
    def __init__(self):
        pass
    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("this is a utility classs for maths operations")

#a=MathUtils
#print(a.add(3,9))
#a.description()

MathUtils.description()
print(MathUtils.add(3,4))

