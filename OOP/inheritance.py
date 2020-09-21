#parent
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def output(self):
        return f'{self.name} is {self.age} years old.'
#child
class Employees(Person):
    def __init__(self,name,age,dept):
        Person.__init__(self, name, age)#inheritance
        self.dept = dept
         
    def in_department(self):
        return f'Is in {self.dept} department.'

emp1 = Employees('Pat', 35, 'Procurement')  
print(emp1.output())      
print(emp1.in_department())