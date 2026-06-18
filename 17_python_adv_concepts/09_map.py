numbers=[1,2,3,45,4,21,25,19]
def square(x):
    return x*x

new=list(map(square,numbers))
print(new)
#using lambda  (lambda used for readablity all thing in singel line so we dont neeed def sqaure stuff things)
old=list(map(lambda y: y*y,numbers))
print(old)