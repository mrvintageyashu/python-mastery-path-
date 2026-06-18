def sum(*args):
    #args will be tuple of all the values passed to sum
    total=0
    for item in args:
        total+=item
    return total

print(sum(2323,23,235,343,4))