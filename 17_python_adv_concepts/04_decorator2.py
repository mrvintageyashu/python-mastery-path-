def decorator(func):
    def wrapper():
        print("amod likes virat kolhi")
        func()
        print("he plays cricket")
    return wrapper

@decorator
def kay_mhantos():
    print("amod fav singer kishor kumar")

@decorator
def say_hello():
    print("kalpesh is best navy sailor")

@decorator
def say_byw():
    print("siddesh doing coding gudd")
    
def say_chesse():
    print("i like to take photos")
    

kay_mhantos()
say_hello()
say_byw()
say_chesses()
