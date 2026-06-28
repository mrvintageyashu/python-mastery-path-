while True:
    try:

        a=int(input("enter the first number"))
        b=int(input("enter the second number"))

        print(f"the division of {a}and {b} is {a/b}")
    except ValueError:
        print("hey dont peform this is not value")

    except ZeroDivisionError:
        print("hey you cant divide by zero bro its error ")
    
    if a<0 or b<0:
        raise ValueError("pls dont peform negative number")
