class P(object):
    def __init__(self,a):
        self.a=a
        print("super",a)
        pass
class C(P):
    def __init__(self,b):
        self.b=b
        print("child",b)
        P.__init__(self,b)
        super(C,self).__init__(4)  
c1=C(3)
