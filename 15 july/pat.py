n=int(input("Enter the number:"))
for x in range(1,n+1):
    for y in range(1,n+1):
        print(chr(64+x),end=" ")#to print pattern from A, 64 initilaizes A
    print()
      
