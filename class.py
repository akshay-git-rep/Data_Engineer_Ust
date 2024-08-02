import datetime

today =datetime.date.today()
year = today.year
"""
print(today)
print(year)
"""

class company():
    def __init__(self,cname):
        self._cname = cname
    def displaycname(self):
        print("company is :", self._cname)
    def address(self):
        return "Shanthiniketean prestige"
"""
c1 = company("ust")

c1.displaycname()
c1.addreess()
"""

class employee(company): # inheritance method 
    ismarried = True
    empcount = 0
    def __init__(self,cname,fname,lname,designation,yob):
        self._cname = cname
        self._fname = fname
        self._lname = lname
        self._designation = designation
        #self._yob = yob
        self._age = year - yob #Encapsulation is _age where its hiding in method
        employee.empcount += 1 
    def getempdetails(self):
        self.displaycname() # inheritance method
        print("fullname:", self._fname,"", self._lname)
        print("age: ", self._age)
        print("designation :", self._designation)
        print("maritial status :", self.ismarried)
    def address(self):
        print("company address is:", super().address()) # polymorphism method
        print("Employee stays in cubbonpet")
        
        

e1 = employee("Carelon","akshay", "pawar", "software engineer", 1995)
e1.ismarried = False

#e2= employee("UST","amruth", "pawar", "dancer", 1992)

e1.getempdetails()
e1.address()
#e2.getempdetails()
#print(employee.empcount) # count the total number of employee














