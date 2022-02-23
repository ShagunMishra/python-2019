class emp:
    state="UP"
    def __init__(self,name):
        self.name=name
    def setAddress(self,address):
        self.address=address
    def getAddress(self):
        return self.address
e1=emp("Abc")
e1.setAddress("Vns UP")
print(e1.getAddress())
