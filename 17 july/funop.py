def sub(a,b):#positional arrgument
    print(a-b)
sub(200,100)
sub(100,200)
#sub(10,20,30) #error because of three arrguments
def cri(name, msg):#keyword arrgument
    print("Hello",name,msg)
cri(name="Virat",msg="GE")
cri(msg="GE",name="Dhoni")#here position doesn't matter
def wish(name='Teacher'):#default arrgument
    print("Hello",name,"GM")
wish("Hemant")
wish("Abc")
wish()#by default name is Teacher
def sum(*all): #variable length arrgument
    total=0
    for n1 in all:
        total=total+n1
    print("The sum=",total)
sum()
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)#any number of arrgument may be given at a time
    
    
