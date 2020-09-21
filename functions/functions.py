def grade_calc(maths, english, science):
    total = maths + english + science
    return total

print(grade_calc(35,80,100))


"""1.Write a function canner_can that takes a single argument item in the form of a 
string, and returns the string 'Can you can a [STRING] as a canner can can a can?', 
where '[STRING]' takes the value of item."""


#option 2
def canner_can(x):
    return f"Can you can a {x} as a canner can can a can?"
print (canner_can("Can"))

"""Define function that calculates the number of seconds in a year."""
def cal_seconds_in_a_year():
    days = 365
    hours_per_day = 24
    second_per_hour = 3600
    number_of_seconds = days*hours_per_day*second_per_hour
    #print(number_of_seconds)
    return number_of_seconds
print(cal_seconds_in_a_year())

"""2.define a function which finds the maximum number among three numbers:"""

# def max_number():
#     mylist = [30,14,60]
#     mylist.sort()
#     x =mylist[len(mylist)-1]
#     return x
# print(max_number())

def max_number(a,b,c):
    if (a >= b) and (a >= c): 
        largest = a 
  
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
          
    return largest 
print(max_number(30,14,60))

def max_number1(mylist1):
    mylist1.sort()
    return mylist1[len(mylist1)-1]
print(max_number1(mylist1 = [30,14,60]))

"""Write a function between_len that takes three arguments:
    a list words;
    an integer minlen; and
    an integer maxlen.
The function should return True if the length of words is at least minlen 
and no more than maxlen, and False otherwise."""

def between_len(words,minlen,maxlen):
    words = ["Lucy", "Kelly"]
    for len(words) in range(minlen,maxlen):
        if len(words)<maxlen and len(words)>=minlen:
            #print("here")
            return True
        else:
            return False
