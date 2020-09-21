#Task1
string = input("Enter a string:")

if string == "yes" or string == "YES" or string == "Yes":
    print("Yes")
else:
    print("No")

#Task2
def mylist4(a):
    return [a[0],a[-1]]
print(mylist4([5, 10, 15, 20, 25]))

#Task3
def odd_even(anyNumber):
    if int(anyNumber)%2 == 0:
        print("{} is an even number".format(anyNumber))
        if int(anyNumber)%4 == 0:
            print("{} is a multiple of 4".format(anyNumber))
    else:
        print("{} is an odd number".format(anyNumber))
odd_even(16)
#Task4
def func_tuple(a_tuple):
    midpoint = int(len(a_tuple)/2)
    firsthalf = a_tuple[:midpoint]
    lasthalf = a_tuple[midpoint:]
    fh_str = str(firsthalf)
    lh_str = str(lasthalf)
    print(fh_str)
    print(lh_str)
    a = fh_str.strip('()')
    b = lh_str.strip('()')
    print(a)
    print(b)

func_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#Task5
def triangle_area(base,height):
    return 0.5*base*height
print(triangle_area(3,5))

#Task6
x = int(input("Enter a number:"))   
if x%2==1:
    print("Weird")
elif x%2==0 and x<=5 and x>=2:
    print("Weird") 
elif x%2==0 and x<=20 and x>=6:
    print("Weird") 
elif x%2==0 and x>20:
    print("Not Weird")    

#PartB
#Task1 list = [2 3 6 6 5]
no_of_students = int(input("Enter number of students:\n"))
scores = input("Enter student scores:\n").split( )[0:no_of_students]# split method splits a string into a list then we slice the list scores to be equivalent to the number of students
new_scores = list(set(scores))#set removes duplicates
new_scores.sort(reverse=True)
print(new_scores[1])

#Part B Task2
#Part B Task3





