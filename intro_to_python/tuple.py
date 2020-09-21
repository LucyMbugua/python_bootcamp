# a tuple is created using ()
# diff btn list and tuple is that, tuple is immutable

dow = ("mon", "tue", "wen", "th", "fri", "sat", "sun")

c = ("mon", [1,2,3], ("Hello", "world"))


# creating a tuple without ()
moy = "Jan", "feb", "march", "april", 

# print(type(moy))

t,y = "Mark",moy
print(y)


# index a tuple
# slice a tuple > +ve -ve
# slice with step

a = ["d", "asd", "asd", [2,3,4,5]]
r,t,y,u=a
print(u)


c = ("Jan", "feb", "march", "april", [1,2,3,4])
c[-1].append(10)
c[-1].append(20)
print(c)