class A:
    def m1(self):
        print("m1() of A")
class B:
    def m2(self):
        print("m2() of  B")
class C(A,B):
    def m3(self):
        print("m3() of C")
c=C()
c.m1()
c.m2()
c.m3()
