class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self, other):
        return point(self.x+other.x, self.y+other.y) 
    def __str__(self):
        return f"{self.x},{self.y}"
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

p1 = point(3, 2)
p2 = point(1, 4)
 
p3 = p1 + p2  # This now works!  It calls p1.__add__(p2)
print(p3)      # Output: (4, 6)  (This uses the __str__ method)
 
print(p1 == p2)
