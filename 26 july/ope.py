class Emp:
    def __init__(self,name,salary):
        self.n=name
        self.s=salary
    def __mul__(self,other):
        return self.s * other.d
class TS:
    def __init__(self,name,days):
        self.n=name
        self.d=days
e=Emp("Abc",500)
t=TS("Abc",25)
print("This month's salary:",e * t)
