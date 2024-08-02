import numpy as np
"""
digits = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ])

arr1 = np.arange(0,25)


print(digits)
print("*"*50)
print(digits.shape)
print("*"*50)
print(arr1.reshape(5,5))
print("*"*50)
r_vector = digits[:,np.newaxis]
print(r_vector)
print("*"*50)
c_vector = digits[np.newaxis:]
print(c_vector)
"""
"""
curve_centre = 80
grades = np.array([20,88,67,98,25])
average = grades.mean()
print(average)
change = curve_centre - grades
print(change)
new_grades = grades + change
print(new_grades)

def curve(grades):
    average = grades.mean()
    change = curve_centre - grades
    new_grades = grades + change
    return np.clip(new_grades,grades,100)

print(grades)
print(curve(grades))
"""
"""
temp = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(2,2,3)
print(temp)
print(temp.shape)
print("*"*50)
print(np.swapaxes(temp,1,2))
print("*"*50)


batting_avarage = np.array([
    [5,75,15,20],
    [25,40,35,30],
    [60,50,55,45],
    [65,70,75,80]
    ])
print("*"*50)
print(batting_avarage.shape)
print(batting_avarage.max())
print(batting_avarage.max(axis=0))
print(batting_avarage.max(axis=1))
print("*"*50)
print(batting_avarage.min())
print(batting_avarage.min(axis=0))
print(batting_avarage.min(axis=1))
"""
"""
#linspace = linear space
numbers = np.linspace(5,51,24,dtype=int)
print(numbers.reshape(4,6))
"""
"""
#arange = arthimetic range
numbers = np.arange(24)
print(numbers.reshape(4,2,3))
print("-"*50)
nums = np.arange(32).reshape(4,1,8)
print(nums)
print("-"*50)
nums_1 = np.arange(48).reshape(1,6,8)
print(nums_1)
print("-" * 60)
print(nums + nums_1)
"""
"""
arr1 = np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr1)
print("*" * 60)
arr2 = np.arange(10,100,5,dtype=int).reshape(3,6)
print(arr2)
sum_of_2_arrays = arr1+arr2
print("Sum of arrays")
print(sum_of_2_arrays)

prod_of_2_arrays = arr1*arr2
print("product of arrays")
print(prod_of_2_arrays)
"""
"""
square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
    ])
for i in range(4):
    print(square[:,i].sum()==35)
    print(square[i,:].sum()==34)
print("-" * 60)
print(square[:2,:2])
print("-" * 60)
print(square[2:,2:])
"""
"""
numbers = np.linspace(5,50,24,dtype="int").reshape(4,-1)
print(numbers)
print("-"*50)
mask = numbers%5==0 #vectorized boolean computation
print(mask)
#filtering
print("all the values divisible by 5 ", numbers[mask]) #converting a resultant array into single dimension
print("all the values divisible by 8 ", numbers[numbers%8==0])

print(numbers.T) #Tranposing
print("Horizontal Sorting", np.sort(numbers,axis=0))
print("Vertical Sorting", np.sort(numbers,axis=1))
"""
"""
a = np.array([[4,8],[6,1]])
b = np.array([[3,5],[7,2]])

print(np.concatenate((b,a)))#merging two array
print("-"*50)
print(np.concatenate((b,a),axis=None))#merging two array and converting it into single dimension array
print("-"*50)
print(np.hstack((a,b)))#horizontal merging of 2 or more arrays
print("-"*50)
print(np.vstack((a,b)))#vertical merging of 2 or more arrays

stock_prices = np.random.random((30,10))
print("stock_prices")
print(stock_prices*10) 
"""
"""
#identity matrix
arr1 = np.eye(4,4)
print(arr1)

#changing type
temperature = np.array([
    [31.8,36.4,11.5],
    [30.2,31.4,0.5]
    ])

tempint = temperature.astype("int") # convert to intiger
tempbool = temperature.astype("bool") # convert to boolen

print(tempint)
print(tempbool)
"""
"""
list1 = [x for x in range(0,101,2)]
print(list1)
arr1 = np.array(list1).reshape(17,3)
print(arr1)
print("-"*50)
"""
"""
arr1 = np.array([1,8,3,2,5])
arr2 = np.array([1,2,3,4,5])
print(np.where(arr1==arr2))
"""
"""
arr = np.full((2,3),5) # get the 5 number in bunch
print(arr)
print("-"*50)

arr1 = np.array([
    [1,2,3],
    [4,5,6]
    ])
newarr1= np.tile(arr1,5) # print 5 time
print(newarr1)
"""
"""
randarr = np.random.randint(0,10,size=(5,5))
print(randarr)
randarr1 = np.random.normal(0,10,size=(5,5))
print(randarr1)
"""
"""
arr1 = ([4,2,8,0])

result= np.argsort(arr1)#get index value of sorted one
print(result)
"""

arr1 = np.array([
    [3,7,9],
    [5,2,4]
    ])
print(np.all(arr1 >= 1))
print(np.all(arr1 >= 10))








































