class A:
    a=10
    def m1(self):
        print("m1() of A")
class B(A):
    b=20
    def m2(self):
        print("m2() of B")
class C(B):
    c=30
    def m3(self):
        print("m3() of C")
d=C()
print(d.a)
print(d.b)
print(d.c)
d.m1()
d.m2()
d.m3()
