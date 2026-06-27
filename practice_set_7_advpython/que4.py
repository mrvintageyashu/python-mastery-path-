class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return (f"title {self.title} by {self.author}")
        
    def __len__(self):
        return len(self.title)
        

b=book("gameofthrones","yash chavan")
print(b)      
print(len(b))  
