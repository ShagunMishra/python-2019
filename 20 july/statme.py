class test:
    a=10
    def __init__(self):
        test.b=20#static variable with class name
    def m1(self):
        test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        test.d2=400
    @staticmethod
    def m3():
        test.e=50
print(test.__dict__)
t=test()
print(test.__dict__)
t.m1()
print(test.__dict__)
test.m2()
print(test.__dict__)
test.m3()
print(test.__dict__)
test.t=60
print(test.__dict__)
        
