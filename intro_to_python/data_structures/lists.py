#python lists
#creating a list of strings
names = ["Daniel", "Janet", "Kevin", "Nelly", "Kenneth"]
#print(type(names))

#list of ints
scores =[90, 70, 80]
#list of floats
weights = [11.2, 34.5, 55.6]
#list of bools
status = [True, False, False]
#mixed list
x = [True, 1, "Mark", 90.6]
#nested list -list inside a list

y = [[10.2, 2, "Brian"], names]
#print (y)
# print(names[3])
# print(names[-2])

z = [ [12,23,[18,True,"8080",["Jane","Mary"], "Hello"] ],"Ken",False,[7,10.2] ]
#print 23
print(z[0][1])
#print Jane, mary
print(z[0][2][3])
#print False
print(z[2])
#print "Hello"
print(z[0][2][4])
#print 8080
print(z[0][2][2])
#print [18,True,"8080",["Jane","Mary"], "Hello"]
print(z[0][2])
#check the length of your string
print(len(z))