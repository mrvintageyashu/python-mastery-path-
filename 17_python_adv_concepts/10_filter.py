def is_greater_than_69(x):
    if x>69:
        return True
    else:
        return False

a=[2,50,70,2026,434,1]
new=list(filter(is_greater_than_69,a))
print(new)
