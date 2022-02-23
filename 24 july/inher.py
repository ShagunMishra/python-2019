class A:
    x=10
    def __init__(self):
        self.b=20
    def m1(self): print("m1() method of A class")
class B:
    z=30
    def __init__(self):
        self.i=40
    def m2(self):
        print("m2() method of B class")
p=A()
q=B()
print(p.x)
print(p.b)
p.m1()
print(q.z)
print(q.i)
q.m2()
    
