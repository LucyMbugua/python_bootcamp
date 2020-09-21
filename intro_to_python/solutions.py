"""
1. Write a Python program to count the occurrences of the word "python" in a given sentence below:
"We are learning how to program in python. I find python programming fun"
"""
# initializing string 
sentence = "We are learning how to program in python. I find python programming fun"

# using count() method to get count  
python_counter = sentence.count('python')

# printing result  
print ("Python occurs " + str(python_counter) + " times in the sentence.") 


"""2.Write a Python function to reverses the word below: reven"""

#Method 1 using join & reverse methods
word = "reven"# initial string
reversedword=''.join(reversed(word))
print(reversedword)

#Method 2 using slicing
stringlength=len(word) # calculate length of the word
slicedWord=word[5::-1] # slicing 
print (slicedWord) # print the reversed string

"""3.Write a program to check if the letter 'e' is present in the word 'Umbrella'."""
#intializing string
word2 = "Umbrella"
#count if any e is available
# e_counter = word2.count('e')
# if e_counter > 0:
#     print("Letter 'e' is present")
# else:
#     print("letter 'e' is not present")

print("e" in word2)

"""4.Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the 
last name which is displayed as it is.For example, if your name is Robert Brett Roser, then the output should be R.B.Roser."""


fName = input("Enter your first name\n")
mName = input("Enter your middle name\n")
lName = input("Enter your last name\n")

print(fName[0]+ "."+ mName[0] + "." +lName)

"""5.Write a python program that checks if each letter in a string begins with a capital letter."""
#Initializing String
institution = "TECHCAMP"
if institution.isupper() == True:
    print("All letters are capital letters")
else:
    print("Not all letters are capital letters")


""" 6.Write a python program to find the index of the first occurrence of a substring in a string below: The worlds fastest plane"""

s = "The worlds fastest plane"
print(s.find("worlds"))#find() function returns the index position of the substring if it’s found


"""7.Write a python program that will check is a string is composed of all string characters as lowercase eg.
'all lower case'.islower() #=> True
'not aLL lowercase'.islower() # False"""

#Initializing String
x = "all lower case"
if x.islower() == True:
    print(True)
else:
    print(False)

"""8. Create a sentence from the following variables """

a = "I"
b = "cant"
c = "wait"
d = "to be"
e = "a"
f = "professional"
g = "python"
h = "programmer"

#String Concatenation or string.format() method
print(a +" "+ b +" "+ c + " " + d + " "+ e +" " + f + " " + g + " " + h)
