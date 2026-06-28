def sum_all(*args):
    total=0
    for item in args:
        total+=item
    return total

print(sum_all(2323,2334,2323,232))

def print_details(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="yash",age=26,city="Los Angeles")