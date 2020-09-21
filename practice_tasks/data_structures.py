"""1. create a program that randomly selects an element from the list below
	numberList = [111,222,333,444,555]"""
import random#random function returns random element from the list
numberList = [111,222,333,444,555]
n = random.choice(numberList)
print(n)

"""2.convert the list above into a tuple"""

numberList = [111,222,333,444,555]
#numbertuple = (111,222,333,444,555)
xy = tuple(numberList)
print(xy)
print(type(xy))

"""3.what is the difference between python append() and extend() methods"""
#append(): Adds its argument as a single element to the end of a list. The length of the list increases by one.
my_list = ['Lucy', 'Ann'] 
my_list.append('Sarah') 
print (my_list)
#output:['Lucy', 'Ann', 'Sarah', [6, 0, 4, 1]]

#extend(): Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.
my_list1 = ['Lucy', 'Ann'] 
another_list = [6, 0, 4, 1] 
my_list1.extend(another_list) 
print (my_list1)
#output:['Lucy', 'Ann', 6, 0, 4, 1]

"""4.create a program that sorts the list below
	ls = [18,2,16,4,1]"""
ls = [18,2,16,4,1]
ls.sort()
ls.sort(reverse=True)
print(ls)

"""5.create a program that counts the occurence of number 4 in the list below
	x=[1, 2, 9, 4, 5, 4, 1]"""
x = [1, 2, 9, 4, 5, 4, 1]
print(x.count(4))

"""6.Select the correct way to access the value of a history subject"""
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict["class"]["student"]["marks"]["history"])

"""7.Create a program that will empty the dictionary below"""
#The clear() method removes all items from the dictionary.
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
student_dict = student.clear()
print(student_dict)

"""8.create a program that will remove 'marks' from the dictionary below"""
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
student.pop("marks")
print(student)
