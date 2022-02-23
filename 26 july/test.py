class test:
    def m1(self):
        print("No Argument Method")
    def m1(self,a):
        print("Single Argument Method")
    def m1(self,a,b):
        print("Double Argument Method")
t=test()
#t.m1()
#t.m1(10)
t.m1(10,20)
#in this case only last statement is executed because python does not support function overloading
