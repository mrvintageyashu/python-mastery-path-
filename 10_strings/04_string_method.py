name='yash chavan'
#name[0]="p" #you cannot do this op in string 

a=len(name)
print(a)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

text=" \nohhhmygoshbydreamm "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

e="python is fun"
print(e.find("is"))
print(e.replace("fun","awesome")) #to replace inside strings 

cars="bmw,mercerdes,audi,ferrari"
print(cars.split(","))
print(",".join(['yash','anil','chavan']))

g="dodge challanger1"
print(g.isalpha())
print(g.isdigit())
print(g.isalnum())
print(g.isspace())