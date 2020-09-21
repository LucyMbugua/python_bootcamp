"""Create a class called Payroll whose major task is to calculate an individual’s Net Salary(Net-Pay)
 by getting the inputs basic-salary and benefits. Create 5 different class methods which will calculate 
the payee (i.e. Tax), NHIFContribution, NSSFContributions, grossSalary and netSalary.
NB: Use KRA, NHIF and NSSF values provided in the link below.
https://www.aren.co.ke/payroll/taxrates.htm  
https://calculator.co.ke/kra-salary-income-tax-paye-calculator"""

class PayRoll():
    
    def __init__(self,basic_salary, car_allowance, house_allowance, nssf,nhif, tax_relief):
        self.basic_salary = basic_salary
        self.car_allowance = car_allowance
        self.house_allowance = house_allowance
        self.nssf = nssf
        self.nhif = nhif
        self.tax_relief = 2400
        self.benefits = 0
        self.total_salary = 0
        self.taxable_salary = 0


    def calc_benefits(self):
        benefits = self.house_allowance + self.car_allowance
        return benefits

    def calc_total_salary(self):
        total_salary = self.basic_salary + self.benefits
        return total_salary

    def calc_taxable_salary(self):
        taxable_salary = self.total_salary - (self.nhif + self.nssf)
        return taxable_salary
    
    def calc_tax(self):
        if self.taxable_salary<=24000:
            tax_bracketA =0.1 * self.taxable_salary
        if self.taxable_salary>24000.0 and self.taxable_salary<=40667.0:
                tax_bracketB = 0.15 *(self.total_salary -24000.0)
                if self.taxable_salary>40668 and self.taxable_salary<=57333:
                    tax_bracketC = 0.20 *(self.taxable_salary - 40668)
                    if self.taxable_salary>57338:
                    tax_bracketD = 0.25 *(self.taxable_salary - 57338)
        return tax_bracketA +tax_bracketB +tax_bracketC +tax_bracketD
        else:
            return 0

        


        

    
        


    
