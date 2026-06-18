a=int(input("enter the first number"))
b=int(input("enter the second number"))

try:
    c=a/b
    print(c)

except Exception as d:
    print(d)

#this is always executed no matter if they completly executes or not 
finally:
    print("this is always executed ")