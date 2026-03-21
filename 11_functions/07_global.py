def sum(a,b):
    print("started dock summming tars its neccesary")
    c=a+b
    global z #this modifiys the global variable man ! 
    z=0
    return c
z=4
print(sum(67,69))
print(z)
