try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print(a/b)
except ZeroDivisionError:
    print("Can not divide by zero.")
except:
    print("Error Occured")
#except ValueError:
    #print("Please provide integer value.")
