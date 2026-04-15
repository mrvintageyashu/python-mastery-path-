class Car:
    location="germany"
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print("speaking now bro")

class BMW(Car):
    def speak(self):
        super().speak()
        print("bruhmmmmmmmm")
            
a=BMW("IIM")
a.speak()