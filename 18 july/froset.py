l1=["Apple","Banana","Mango"]
print(l1)
l1[0]="Cheery"
x=frozenset(l1)
print(x)#value of list get copied in list
# x[0]="Apple" #error because can not initialize value in frozen set 
