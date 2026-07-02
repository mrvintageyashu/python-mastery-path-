#if we used  with we dont need to use f.close() and simple syntax
with open("yash.txt","r") as f:
    content=f.read()
    print(content)