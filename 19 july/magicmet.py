class stu:
    " " "This is student class, define details of student." " "
    c=5
    def __init__(self,name,age,roll):
        self.Name=name
        self.Age=age
        self.Roll=roll
    def m1(self):    
        self.c
        print(self.c)#inside instance method calling class variable
    def display(self):
        print("Name:%s"%self.Name,"\nAge:%d"%self.Age,"\nRollno:%d"%self.Roll)
        print("Name:%s,Age:%d,Rollno:%d"%(self.Name,self.Age,self.Roll))
s1=stu("XYZ",25,101)
s2=stu("ABC",30,102)
print(stu.__doc__)#to access doc value or class detail
print(stu.__dict__)#to access dictionary info of class
print(s1.__dict__)#to print info of s1 object in dictionary format
print(stu.__module__)#to access the module in which class is defined
print(stu.__name__)#used to access the name of the class
print(stu.__bases__)#used to access tuple including base class
s1.m1()
s1.display()
