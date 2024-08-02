from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict
"""
#namedtuple
courses = namedtuple("course",["name","tech"])
print(courses)
clist = courses(name="data science",tech="python")
print(clist) # display whole 
print(getattr(clist,"tech")) #display tech value
print(clist.name) # display the value
print(clist[1])  #based on key name entered
newlist = ["web sevelopment", "angular"]
print(courses._make(newlist)) # converted newlist to tuple
#deque
list1 = ["akshay","bharath","chethan"]
print(list1)
lqueue = deque(list1)
print("original:",lqueue)
lqueue.appendleft("sudhir") #append = add to right, #appendleft = add to left
print("append at right:", lqueue)
lqueue.popleft()#pop = delete at right, popleft = delete on left
print("POP :", lqueue)
#Chainmap
dict1 = {1:"akshay", 2:"bharath"}
dict2 = {3:"chethan", 4:"deepak"}
join_dict = ChainMap(dict1,dict2)
print(join_dict)
dict3 = {4:"english",6:"fun"}
update_dict = join_dict.new_child(dict3)
print(update_dict)
print("*"*50)
print(update_dict.maps)
print("*"*50)
print(list(update_dict.keys()))
print("*"*50)
print(list(update_dict.values()))
"""
#counter
score = [18,25,67,18,25,67,95]
score_count = Counter(score)
print(score_count)
print(score_count.keys())
print(score_count.values())
print(score_count.items())
#default dict
tempd = defaultdict(int)
tempd[0] = "akshay"
tempd[1] = "bharath"
print(tempd)
print(tempd[0])
print(tempd[1])
print(tempd[2]) # when we dont have index we get 0 as default
#ordered dict
clist = OrderedDict()
clist["akshay"] = 100
clist["bharath"] = 90
clist["chethan"] = 80
clist["deepak kumar sharma"] = 70
for key,value in clist.items():
    print(key,value)
print("*"*50)
clist["akshay"] = 50 #value got changed from 100 to 50
for key,value in clist.items():
    print(key,value)
clist1 = OrderedDict()
clist1["akshay"] = 100
clist1["bharath"] = 90
clist1["chethan"] = 80
clist1["deepak kumar sharma"] = 70
print(clist == clist1)










































