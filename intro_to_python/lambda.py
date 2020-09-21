"""
keyword lamda
sytax:
lambda parameters:expression
points to note:
*can have any number of parameters but only one expression
"""

# def addtwo(num1):
#     return num1+2
# print(addtwo(2))

#using lambda
add_two = lambda num1: num1+2
print(add_two(2))

to_upper = lambda str1: str1.upper()
print(to_upper("techcamp"))

# def even_odd(number:int)->str:#takes type int returns string
#     if number%2==0:
#         return "even"
#     else:
#         return "odd"
#comprehension of the above even_odd function
even_odd = lambda num:"even" if num%2==0 else "odd"

# def weird_funct(number:int, value_to_add:int)->int:
#     """this function takes two arguments...."""
#     return number+value_to_add
#comprehension of the weird_funct function 
weird_funct = lambda number,value_to_add:number+value_to_add

print(even_odd(3))
print(weird_funct(2,5))