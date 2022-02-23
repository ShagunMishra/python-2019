fl=dict({"fl11":"Apple","fl2":"Mango","fl3":"Banana","fl4":"Grapes"})#dictionary consturctor
print(fl)
a=fl.copy()#to copy value of dictionary
print(a)
b=dict(fl)#another way to copy value of dictionary
print(b)
square={x:x*x for x in range(1,6)}#dictionary comprehension
print(square) #to find square
double={x:2*x for x in range(1,6)}#to find double
print(double)
