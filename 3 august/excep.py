a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
try:
    c=a+b
    print(c)
    d=a-b
    print(d)
    e=a/b
    print(e)
except ZeroDivisionError:
    print("Error in division")
f=a*b
print(f)
