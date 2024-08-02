import numpy as np
"""
arr1 = np.arange(0,20).reshape(4,5)
print(arr1)
print("max value :",arr1.max())
print("min value :",arr1.min())
print("max value from column :",arr1.min(axis=0))
print("max value from row :",arr1.min(axis=1))
"""
"""
arr1 = np.array([
    [3,7,1],
    [10,3,2],
    [5,6,7]
    ])

print(arr1)
print("sort whole array")
print(np.sort(arr1,axis=None))
print("sorting row wise")
print(np.sort(arr1,axis=1))
print("sorting column wise")
print(np.sort(arr1,axis=0))
"""
"""
list1 = [
    np.array([3,2,8,9]),
    np.array([4,12,34,25,78]),
    np.array([23,12,67])
    ]

print(len(list1),list1)
print("-"*50)
result = []
for i in range(len(list1)):
    result.append(float(np.mean(list1[i])))
print(result)
"""
"""
arr1 = np.array([
    [3,2,8],
    [4,12,34],
    [23,12,67]
    ])
newrow = ([5,5,5])
new_arr = np.vstack((arr1,newrow))
print(new_arr)
"""
"""
arr1 = np.array([5,8,2,5])
print(arr1)
reversearr1 = np.flip(arr1)
print(reversearr1)
"""
"""
arr11 = np.array([
    [3,2,8],
    [4,12,34],
    [23,12,67]
    ])

arr22 = np.array([
    [3,2,8],
    [4,12,34],
    [23,12,67]
    ])

result = np.dot(arr11,arr22)
print(result)
#print(arr11 * arr22)
"""
"""
n = 8
arr1 = np.zeros((4,4),dtype="int")
arr2 = np.zeros((n,n),dtype="int")
#print(arr1)
arr1[::2,1::2] = 1
arr1[1::2,::2] = 2
print(arr1)
for i in range(4):
    print("\nthis is i :",i)
    for j in range(4):
        print("\nthis is j:",j)
        print(arr1[i][j],end="")
    print()
"""




























