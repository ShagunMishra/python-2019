class A:
    a=1
class B:
    b=2
class C:
    c=3
class D(A,B,C):
    d=4
class E(D):
    e=5
class F(E):
    f=6
class G(F):
    g=7
class H(F):
    h=8
x=F()
print(x.a,x.b,x.c,x.d,x.e,x.f)
y=G()
print(y.g)
z=H()
print(z.h)
    
    
