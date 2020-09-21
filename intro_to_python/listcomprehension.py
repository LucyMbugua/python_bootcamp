# x =  [1,2,3,4]
# new_list =[]

# for each in x:
#     new_list.append(each *2)
# print(new_list)

"""The above can be done using list comprehension
easy way to create lists from an existing list
Syntax
[expression for variable in x
where x can be list or a string"""
#comprehension of the list above 
list1 =  [1,2,3,4]
new_list =[x for x in list1]
print(new_list)

#create a list where each character is an element in the string
name ="techcamp"
# name_list =[]
# for i in name:
#     name_list.append(i)
# print(name_list)

#comprehension of the list above 
name_list =[char for char in name]
print(name_list)

"""construct list comprehensions that have conditional statements"""
#Generate a list of all even numbers from 1 to 10
# even_numbers_list =[]
# for each in range(1,11):
#     if each%2 ==0:
#         even_numbers_list.append(each)
# print(even_numbers_list)

#comprehension of above list
even_numbers_list =[num for num in range(1,11) if num%2 ==0]
print(even_numbers_list)

#generate list of odd numbers 90 to 100
odd_numbers_list =[num for num in range(90,101) if num%2==1]
print(odd_numbers_list)



list2 = [x*2 if x%2 ==0 else x*3 for x in range(1,11)]
print(list2)