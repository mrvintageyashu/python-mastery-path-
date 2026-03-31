coordinates=(10,20)
print(coordinates[0])
print(coordinates[1])

#coordinates[0]=50 tuple cant be changed
corlist=list(coordinates)
corlist[0]=50
print(corlist)
coordinates=tuple(corlist)
print(coordinates)