class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print(self.name)
p1=person("Abc",35)
p1.myfun()
