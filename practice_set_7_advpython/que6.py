numbers=[1,2,3,4,5]
def cube(x):
    return x**3
new=list(map(cube,numbers))
print(new)


def filter_out_evens(x):
    if x%2==0:
        return True
    else:
        return False
a=[10,11,12,13,14]
newa=list(filter(filter_out_evens,a))
print(newa)