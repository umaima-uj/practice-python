class book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __str__(self):
        return f"book: {self.title}" 
    def __len__ (self):
        return self.pages
    def __eq__(self,other):
        return self.title==other.title
b1=book("python 101",540)
b2=book("python 102",700)
print(b1)
print(len(b1)) 
print(b1==b2)
   