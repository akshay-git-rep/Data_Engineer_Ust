"""
try:   
    num1 = int(input("enter the number 1 :"))
    num2 = int(input("enter the number 2 :"))
    result = num1/num2
    print(num1/num2,"=",result)

    prime_numbers = [12,15,17,19]
    prime_numbers[len(prime_numbers)] = 12
    print(prime_numbers)

    num = int(input("Enter the even number :"))
    assert num % 2 == 0
    
except ZeroDivisionError:
    print("Error: Dominator can't be zero")

except IndexError:
    print("Error: given index is not present please use append or insert method")

except AssertionError:
    print("Error: you have entered odd number")
    
else:
    print(num)
"""
"""
yob = int(input("Enter the year of birth:"))
age = 2024 - yob

if age < 18:
    raise Exception(f"Your age is {age} and come after your age is 18")
else:
    print("eligible for voting")
"""

def divide(x,y):
    try:
        if y == 0:
            raise ZeroDivisionError("Denominator shouldn't be 0")
        result = x/y
        return result
    except (ZeroDivisionError, AssertionError) as e:
        print("error:",e)
    #except ValueError:
    #    print("error:please enter number")
        

x = int(input("Emter num1:"))
y = int(input("enter num2:"))
print(divide(x,y))
    
























