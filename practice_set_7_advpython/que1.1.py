def decorator(func):
    def logger():
        print("function is been called")
        func()
        
    return logger

@decorator
def say_hello():
    print("hello")

say_hello()