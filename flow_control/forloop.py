ls = [10,20,20,40]

for element in ls:
    #print(element)
    pass

for char in "techcamp":
    #print(char)
    pass

student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}
for each in student:
    #print(each,student[each])
    #print("Key : {} , Value : {}".format(each,student[each]))
    pass

for k,v in student.items():#unpacking the dictionary
    #print(k,v)
    pass

for number in range(1,11):
    #print(number)
    pass

#find the sum of all even numbers from 10 to 20
evensum = 0
for number in range(10,21):
    if number%2==0:
        #evensum = evensum +number
        evensum+=number
        
        #number+=number
print(evensum)



#find the sum of all odd numbers from 10 to 20
oddsum = 0
for number in range(10,21):
    if number%2==1:
        #evensum = evensum +number
        oddsum+=number
        
        #number+=number
print(oddsum)