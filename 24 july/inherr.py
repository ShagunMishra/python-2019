class P:
    def m1(self):
        print("m1() of P")
class C(P):
    def m2(self):
        print("m2() of C")
class D(P):
    def m3(self):
        print("m3() of D")
d=D()
d.m1()
#d.m2()
d.m3()
