class Emp:
    " " "Developed for this class to represent employee details." " "#doc value can be accessed directly
    def __init__(self):#constructor initialize by python
        self.name="Shag"
        self.age=20
        self.id=101
        self.salary=501
    def talk(self):#to print all value
        print("Hello I am",self.name)
        print("My age is:",self.age)
        print("My ID is:",self.id)
        print("My salary is:",self.salary)
e1=Emp()#variable is assigned to class
e1.talk()#through assigned variable function of class is get called
print(Emp.__doc__)#to call doc value
