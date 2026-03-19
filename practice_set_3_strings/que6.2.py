a=str(input("enter a stirng to check palindrome or not: "))
a=a.lower()

if(a==a[::-1]):
        print("its the palindrome number")
else:
        print("nahh its not palindrome number")
        