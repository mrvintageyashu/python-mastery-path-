from functools import reduce
num=[1,2,3,5,6]
def product(a,b):
    return a*b
c=reduce(product,num)
print(c)