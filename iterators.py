#Iterator
"""
list1 = [1,23,4,5,6,7,8,9]
list_itr = iter(list1)
print(next(list_itr))
print(next(list_itr))
for i in list_itr:
    print(i)
"""
#generator
def c_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

value = c_generator(5)

print(next(value))
print(next(value))
print(next(value))
print("*"*10)
for i in c_generator(5):
    print(i)
