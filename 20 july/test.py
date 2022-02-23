class test:
    x=10
    def __init__(self):
        self.y=20
t1=test()
t2=test()
print("t1",t1.x,t1.y)
print("t2",t2.x,t2.y)
test.x=99
t1.y=12
print("t1",t1.x,t1.y)
t1.x=23
print("t1",t1.x,t1.y)
