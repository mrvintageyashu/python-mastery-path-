def sum(a,b):
    c=a+b
# a and b now local variable 
    return c

z=8 #z is now global variable even it value cant change even its in fxn
print(z)
print(sum(4,2))
print(z)
