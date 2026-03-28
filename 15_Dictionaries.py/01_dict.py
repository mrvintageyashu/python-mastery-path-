sgpa={"yash":8.05,"sujal":7.64,"sainath":9}
print(sgpa,type(sgpa))

print(sgpa["yash"])
sgpa["yash"]=9.5
print(sgpa)
print(sgpa.keys())
print(sgpa.values())
sgpa.pop("sujal")
print(sgpa)