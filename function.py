salary_allowance = {"HRA" : 0.4, "DA": 0.3, "TA":0.15}
standared_deduction = {"PF":0.12, "insurance":5000}

def calcAllowances(basic):
    total_allowances = 0

    for key in salary_allowance:
        total_allowances += salary_allowance[key]*basic
    return total_allowances

def calcDeduction(basic):
    total_deduction = 0

    for key in standared_deduction:
        if type(standared_deduction[key]) is not int:
            total_deduction += standared_deduction[key]*basic
        else:
            total_deduction += standared_deduction[key]
    return total_deduction

def pTax(mSal):
    prof_tex = 0

    if mSal >=8500 and mSal <= 10000:
        prof_tax = 200
    elif mSal > 10000 and mSal <= 30000:
        prof_tax = 300
    elif mSal > 30000:
        prof_tax = 500
    return prof_tax

def calculateSalary(bsal):
    #bsal = int(input("Enter the basic salary :"))
    gsal = bsal + calcAllowances(bsal)
    p_tax = pTax(gsal)
    n_sal = gsal - calcDeduction(bsal) - p_tax
    print("Basic Salary:", bsal)
    print("allowances :", calcAllowances(bsal))
    print("prof_tax :", p_tax)
    print("deductions:", calcDeduction(bsal))
    print("gross Salary:", gsal)
    print("net salary:", n_sal)

#calculateSalary()

