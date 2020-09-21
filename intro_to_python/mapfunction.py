
"""
Map is an inbuilt function whose parameters is function and list
map(function, list)
list, lst below is the iterable
"""
list1 = [1,2,3,4]
new_list =list(map(lambda number: number*2, list1))
print(new_list)#<map object at 0x0000023C3AAFC288> says we have a map object at a certain memory location henc we wrap it on a list


lst = [1,-1,2,3,4,-3,-4,-5,-6]
negative_nums =list(filter(lambda number:number<0, lst))
print(negative_nums)

#Write a code to get product of list below
from functools import reduce, wraps #reduce requires to be imported
ls = [1,2,3,4,5]
#reduce applies a rolling computation
product = reduce(lambda a,b:a*b, ls)
print(product)
