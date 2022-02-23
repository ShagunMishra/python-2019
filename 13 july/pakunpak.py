a=10
b=20
c=40
d=30
t=a,b,c,d
print(t)#packing
t1=(1,2,3,4)
a,b,c,d=t
print("a =",a,"b =",b,"c =",c,"d =",d)#unpacking
t=(x**2 for x in range(1,6))#to print square of the number **sign means raise to the power
print(type(t))
for x in t:
    print(x)
