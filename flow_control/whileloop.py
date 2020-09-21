# i = 0
# while True:
#     count+=1
#     print(f"{count} "its true");

# 
"""
sum = 0
i=10
while i>0:
    sum+=i
    print(i)
    i-=1
    
print("The sum of the numbers is"+ " ",sum)"""
""""
CREATE A CONSOLE APPLICATION THAT DOES THE FOLLOWING

-ask the user to set their pin.
-the user has 3 attempts to login.
-if the user enter the wrong pin, he can reenter it again and display the number 
of attempts left.
-if attempts are exhaused, display sim blocked

"""
set_pin = int(input("Set your pin:"))
i = 3
while i>0:
    pin = int(input("Enter your pin:"))
    
    if pin==set_pin:
        print("login successful")
        break
    elif pin!=set_pin:
        i-=1
        if i==0:
            print("sim blocked")
        else:
            print("You have",i,"attempts left")
        

    
    




