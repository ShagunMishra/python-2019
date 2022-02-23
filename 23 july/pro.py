n=int(input("Enter the number of students:"))
d={}
for i in range(n):
    name=input("Enter the student name:")
    marks=input("Enter the marks of student:")
    d[name]=marks
while True:
    name=input("Enter student name to get marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("Student not found.")
    else:
        print("The marks of ",name,"are",marks)
    option=input("Do you want to find another student marks:[Yes/No]")
    if option=='No':
        break
    elif option=='Yes':
        continue
    else:
        break
print("Thanks for using our application.")
