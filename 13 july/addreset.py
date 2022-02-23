cl={"Red","Orange","Blue","Yellow","Green"} #there is no any index position of set they always change there index position
print(cl)
cl.add("Purple") #to add element in the set
cl.add(1)
print(cl)
cl.update({"Orange","Mango","Banana"})
print(cl) #no any repeated value allowed in set
print(len(cl))#to get length of the set
cl.remove("Mango")#to remove item from set show error when item not exist
print(cl)
cl.discard(1)#to remove or discard item form set not show amy error if item not exist
print(cl)
x=cl.pop()#random value because of the set 
print(x)



       
