class P:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls): print("Parent class method")
    @staticmethod
    def m3():
        print("Static method")
class C(P):
    pass
c=C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
class D(C):
    pass
d=D()
print(d.b)
d.m2()
        
