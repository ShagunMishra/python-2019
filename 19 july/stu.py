class student:
    def __init__(self,rollno,name,clas):
        self.roll=rollno
        self.nam=name
        self.cla=clas
    def talk(self):
        print("Roll No:",self.roll)
        print("Name:",self.nam)
        print("Class:",self.cla)
s1=student(1,"Ashish","4th")#s1 is the object to call class
s1.talk()
        
