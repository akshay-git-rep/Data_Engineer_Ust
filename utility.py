def leapyear(year):
    if (year * 400 == 0 or (year%100!=0 and year%4==0)):
        return str(year) + "its a leap year"
    else:
        return str(year) + "its not a leap year"

payment_mode = ["online", "offline"]
gender = ["male", "female", "other"]

def add(a,b):
    return a + b
