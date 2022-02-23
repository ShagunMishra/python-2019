class Student:
    def __init__(self,name,age,address):
        self.name1=name
        self.age1=age
        self.address1=address
    def show(self):
        print(self.name1)
        print(self.age1)
        print(self.address1)
s1=Student("Kushal",12,"Varanasi")
s1.show()
s2=Student("Muskan",20,"Delhi")
s2.show()
