def decorator(func):
    def wrapper():
        print("i am about to write the function brother")
        func()
        print("i have executed the this execcution")
    return wrapper

@decorator  
def say_hello():
    print("hello")

#f=decorator(say_hello)
#f()
say_hello()
