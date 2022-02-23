def sp(n):
    c="*"
    for i in range(n):
        print((c*i).rjust(n-1," ")+c+(c*i).ljust(n-1," "))
sp(5)        
