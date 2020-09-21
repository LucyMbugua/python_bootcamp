"""

Python lists
* use [] to create a list

** sequences -> string, list,tuple
"""

# creating a list of strings
names = ["Daniel", "Janet", "Kevin", "Nelly", "Kenneth"]
# list of ints
scores = [90,70,80]
# list of float
weights = [11.2,33.5,17.8]
# list of bools
status = [True,True,False,False]
# mixed list
x = [True,"Mark", 90.8,17.2, 12,False,True]
# nested list - list inside a list
y = [[10,2,"Brian"], names]

"""
How to access elements inside a list?

*use list indexing - [x] -> index of the element
"""
# print Nelly from names list
# print(names[3])
# print(names[-2])

# z = [ [12,23,[18,True,"8080",["Jane","Mary"], "Hello"] ], "Ken", False, [7,10.2] ]
z = [[12,23,[18,True,"8080",["Jane","Mary"], "Hello"]], "Ken", False, [7,10.2] ]

# print 23  -> Nelly

# print ["Jane","Mary"] -> Kenneth
# print(z[0][2][3])
# print False -> Lucy
# print(z[2])
# print "Hello" -> Kevin
# print(z[0][2][4])

# print [18,True,"8080",["Jane","Mary"], "Hello"] -> Janet
# print(z[0][2])

# check the length of your string  "Mary" -> Daniel
# mary = z[0][2][-2][-1]
# print(len(mary))

# print("len of list z:", len(z))


# list slicing -> obtain a range of element in ur list
cars = ["subaru", "Toyota", "Mazda", "premio", "Pajero"]
# print(cars[2:])

# slicing with step
# print(cars[::2])

# lists are mutable
# 1. use of assignment operator =
cars[-1] = 100
# print(cars)

# 2. use the append() method
cars.append(300)
print(cars)

# research on list manipulation methods
# 3. pop(), remove(),

# remove element from list
del cars[1]
print(cars)

x = [1,2,3]
y = [4,5,6]
z = x+y
print(z)

z.insert(3, "ken")

print(z)
# list comprehension

# ORM

# membership operator (in , not in)
print(7 not in z)