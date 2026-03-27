def safe_divide(a,b):
    if (b==0):
        return print("it cant be divide by zero")
    else:
        return a//b
        

a1=float(input("enter the no1: "))
b1=float(input("enter no 2: "))
result=safe_divide(a1,b1)
print(result)
