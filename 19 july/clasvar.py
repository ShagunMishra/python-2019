class student:
    stream="CS"#class variable
    def __init__(self,roll):
        self.roll=roll#instance variable
s1=student(100)#object of student class
s2=student(101)
s3=student(102)
print(s1.roll)
print(s2.roll)
print(student.stream)
print(s1.stream)
