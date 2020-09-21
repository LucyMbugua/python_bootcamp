class HumanBeings():#initializig a class

    def __init__(self,name, color,height,weight,age):#used to create all parameters to be used in this class
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight
        self.age = age
        self.bmi = 0
    #creating methods - functions that are related
    def get_result(self):
        return f'{self.name} is of {self.color} - color, {self.height} - height, {self.weight} - weight, {self.age} - age'
    
    def calc_bmi(self):
        height_meters = self.height/100
        self.bmi = self.weight/(height_meters*height_meters)
        return self.bmi

    
    #Give user advise based on BMI output(normal, abnormal bmi)
    def bmi_advise(self):
        bmi =self.bmi
        if bmi<18.5:
            return f"You are int the underweight range"
        elif bmi<25.0 and bmi>=18.5:
            return f"you're in the healthy weight range"
        elif bmi<30.0 and bmi>=25.0:
            return f" you're in the overweight range"
        elif bmi>=30.0:
            return f"you're in the obese range"


#intantiation
person1 = HumanBeings(name = 'lucy', color = 'Black', height =170, weight =70, age =28)
# person2 = HumanBeings('White', 130, 32)
print(person1.get_result())
print(person1.calc_bmi())
print(person1.bmi_advise())
# print(person2.get_result())