from functools import reduce
num=[1,2,3,4,5,6]
"""
addition of  1+2+3+4+5+6=21 
reduce take function as argument 

"""
def sum(a,b):
    return a+b

c=reduce(sum,num)
print(c)