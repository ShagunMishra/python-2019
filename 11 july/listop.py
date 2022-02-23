num=[1,2,3,4,5,1,3,4,5,1,2,1,4]
print(num)
l1=["Hello",1,'Abc',True,2.5,"Apple",False]
print(l1)
l2=[10,20,30,40,50,60,70]
print(l2)
print(l2[0])
print(l2[-1])
print(l2[1:3])#to print from range 1 to 2
print(len(l2))#to print length of the list
l3=["Hi","Hello",1,2,3,"Mango","Banana",2.4]
print(len(l3))
l1.append(2.7)#to add item in list
print(l1)
l3.insert(2,"C++")#to insert on a particular position
print(l3)
l3.remove("Hello")#to remove specified item
print(l3)
l3.pop()#to remove index by default it remove last item
print(l3)
print(l3.pop(2))#to remove specified index
print(l3)
del l3[2]# to remove particular index
print(l3)
del l3 # to remove whole list
# print(l3) show error because l3 is removed from the list
num.clear()#to clear all item in the list
print(num)
l3=l2.copy()# to copy list in the another list
print(l3)
l4=list(l1)# another way of copy list
print(l4)


