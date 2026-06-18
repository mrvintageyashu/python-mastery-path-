def marks(**kwargs):
    #kwargs is dictonary with all the key value pairs whch passed to marks 
    for items in kwargs.keys():
        print(f"the marks of {items} are {kwargs[items]}")

marks(yash=40,sujal=40,sanjana=37,piyush=35,dhanshree=36)
