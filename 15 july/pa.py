n=int(input("Enter the number:"))
for x in range(1,n+1):
    for y in range(1,n+1):
        print(chr(96+x),end=" ")#to print small alphabets
    print()
      
