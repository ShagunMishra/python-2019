a=10#global variable can be accessed anywhere
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()
def m1():
    b=20#local variable only accessed in m1
    print(b)
'''def m2():
    print(b)'''#error because b is defined in m1
m1()
#m2()
def p1():
    global c#global variable can be defined inside function 
    c=30
    print(c)
def p2():
    print(c)
p1()
p2()
    
    
