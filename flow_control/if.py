"""if 10>20:
    #print("10 is greater than 2")"""

#create an app that checks if a number is positive or negative
x = int(input("Enter a random number:"))   
if x>0:
    print(x, "is a positive number")
elif x==0:
    print("the number is zero")    
else:
   # print(x, "is a negative number")
    print(f"{x} is a negative number")