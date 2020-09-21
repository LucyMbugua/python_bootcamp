#TASK 1:
# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
# Hint: Use input () to get the persons input

string = input("Enter a string:")

if string == "yes" or string == "YES" or string == "Yes":
    print("Yes")
else:
    print("No")

"""TASK 2: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function"""

# a = [5, 10, 15, 20, 25]
# mylist = [a[0],a[-1]]    
# #mylist.append(a[0]) 
# #mylist.append(a[len(a) -1]) 
# print (mylist)

def mylist4(a):
    return [a[0],a[-1]]
print(mylist4([5, 10, 15, 20, 25]))

"""TASK 3:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
1.	If the number is a multiple of 4, print out a different message."""

# number = int(input("Enter a number:"))

# if number%4==0 and number%2==0:
#     print(number, " is a multiple of 4")
       
# elif number%2==1:
#     print(number, " is odd")
# elif number%2==0:
#     print(number, " is even")

#num = int(input("Enter a number: "))
"""check = 4

if (num%2)==0:
   print("{0} is even".format(num))
else:
   print("{0} is odd".format(num))
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)"""

"""# Ask the user for any number
anyNumber = input("Enter a number:")
# evalute the number and print out appropriate messages.
if int(anyNumber)%2 == 0:
    print("{} is an even number".format(anyNumber))
    if int(anyNumber)%4 == 0:
        print("{} is a multiple of 4".format(anyNumber))
else:
    print("{} is an odd number".format(anyNumber))"""

def odd_even(anyNumber):
    if int(anyNumber)%2 == 0:
        print("{} is an even number".format(anyNumber))
        if int(anyNumber)%4 == 0:
            print("{} is a multiple of 4".format(anyNumber))
    else:
        print("{} is an odd number".format(anyNumber))
odd_even(16)


