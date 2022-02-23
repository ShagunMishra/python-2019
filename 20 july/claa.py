class test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t=test()
t.m1()
print(t.__dict__)
t.d=40
print(t.__dict__)
print(t.a,t.b)
