def sum_digits(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum_digits(n//10)


    

a=int(input("enter the number to sum of digits"))
sum_digits(a)
totalsum=sum_digits(a)
print("the toatl sum : ",totalsum)

    
