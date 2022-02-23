def fact(x):
    a=1
    for i in range(1,x+1):
        a=a*x
        x=x-1
    return(a)    
y=int(input("Enter the number:"))
print("Factorial is:",fact(y))
