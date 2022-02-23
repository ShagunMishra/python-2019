def myfn(n):
    return lambda a:a*n
mydu=myfn(2)#value of this function get stored in a
print(mydu(4))#value of this function get stored in n
print(mydu(100))
