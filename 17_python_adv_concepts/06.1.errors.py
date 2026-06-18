a = int(input("enter the first number : "))
b = int(input("enter the second number: "))
if b==0:
    raise ValueError("please dont divide by zero ")
print(f"the division is {a / b}")