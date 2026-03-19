sen="you are very good boy"
sum=0
vowels=['a','e','i','o','u']
for char in sen.lower():
    if char in vowels:
        sum=sum+1
    
print(f"the total vovwels are {sum}")