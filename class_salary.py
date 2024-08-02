class salary:
    salary_allowance = {"HRA" : 0.4, "DA": 0.3, "TA":0.15}
    standared_deduction = {"PF":0.12, "insurance":5000}
    
    def __init__(self,basic):
        self._basic = basic

class allowances(salary):
    def __init__(self):
        super().__init__(basic)
        
    def calc_allowance(self):
        total_allowances = 0
        
        for key in salary.salary_allowance:
            total_allowances += salary.salary_allowance[key] * self.basic
        return total_allowances

class deduction(salary):

    def __init__(self):
        super().__init__(basic)
        
    def calc_Deduction(self):
        total_deduction = 0

        for key in salary.standared_deduction:
            if type(self.standared_deduction[key]) is not int:
                total_deduction += salary.standared_deduction[key] * self.basic
            else:
                total_deduction =+ salary.standared_deduction[key]
            return total_deduction

class prof_tax(salary):
    prof_tax = 0

    def calc_prof(self):
        if self.basic >= 8500 and self.basic <= 10000:
            prof_tax = 200
        elif self.basic > 10000 and self.basic <= 30000:
            prof_tax = 300
        elif self.basic > 30000:
            prof_tax = 500
        return prof_tax
class total_salary(allowances,deduction,prof_tax):
    prof_tax = 0
    def __init__(self,basic):
        self.basic = basic

    def calc_total_salary(self):
        #self.basic= int(input("enter the basic salary:"))

        gsal =  self.basic + self.calc_allowance()
        nsal = gsal - self.calc_Deduction() - super().calc_prof()


        print("basic salary :", self.basic)
        print("total allowance:", super().calc_allowance())
        print("gross salary:", gsal)
        print("total deduction:", super().calc_Deduction())
        print("prof tax:", super().calc_prof())
        print("net salary:", nsal)
        

s1 = total_salary(10000)
s1.calc_total_salary()

    





