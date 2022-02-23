t=[1,3,6,4,8,7,6,1,2,9,5,8,4,1,7,8,9]
print("Given list is:")
print(t)
a=0
b=0
for x in t:
    if(x%2==0):
        a=a+1
    else:
        b=b+1
print("Even numbers present in list is:",a)
print("Odd numbers present in list is:",b)
        
