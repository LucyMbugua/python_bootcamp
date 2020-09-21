
firstName = 'Lucy'
lastName = "Wanjiku"

print(type(firstName))
print(type(lastName))

#string indexing = retrieve certain character from a string
#positive indexing
print(firstName[0])
print(firstName[3])

#negative indexing 
print(firstName[-4])

#string slicing
institution = "Techcamp"
#positive slicing
print(institution[0:4])
print(institution[4:8])

#Negative slicing
print(institution[-8:-4])
print(institution[-4:])

#slicing with step
print(institution[::3])

#string concatention
a = "tech"
b = "CAMP"
c = "Kenya"

fullName = a+b+c
print(fullName)

print(a.upper())
print(b.lower())
print(a.title())
