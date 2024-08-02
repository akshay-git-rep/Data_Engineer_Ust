year = int(input("enter the year: "));
#print(type(year))
"""
if (year%400 == 0):
    print(year, "its a leap year")
else:
    if (year %100 != 0):
        if (year % 4 == 0):
            print(year, "its a leap year")
        else:
            print(year, "its not a leap year")
    else:
            print(year, "its not a leap year")
"""
"""
if (year%400 == 0):
    print(year,"its a leap year")
elif (year % 100 != 0 and year % 4 == 0):
    print(year, "its a leap year")
else:
    print(year, "its not a leap year")
"""
if (year % 400 == 0 or (year % 100 != 0 and year%4==0)):
    print(year,"its a leap year")
else:
    print(year,"its not a leap year")
