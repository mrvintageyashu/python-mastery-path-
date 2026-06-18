while True:
    try:
        a = int(input("enter the first number : "))
        b = int(input("enter the second number: "))

        print(f"the division is {a / b}")
    except ZeroDivisionError:
        print("hey dont divide by 0")
    except ValueError:
        print("please dont peform bad calculations bad typecast")
    except Exception as e:
        print("some error occured", e)


