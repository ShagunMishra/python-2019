class  Book:
    def __init__(self,page):
        self.p=page
    def __add__(self,other):
        return self.p + other.p
b1=Book(100)
b2=Book(200)
print("The total no. of pages:",b1+b2)
    
