my_stock = {} #empty  dictionary
my_stocks = {"TCS":2700,"infosys":3000,"IDBI":2500}
#print(my_stocks[0]) #we get error bcz we cant find using index for dictionary
print(type(my_stocks))
print(my_stocks)
my_stocks["SBI"] = 1700
print(my_stocks)
print("length of my stock is:",len(my_stocks))
print("show stock name",my_stocks.keys())
print("show stock values",my_stocks.values())
print("print value of Infosys:",my_stocks["infosys"])

print("=" *10)
for stock in my_stocks:
    print(stock,"price is: ", my_stocks[stock])
print("=" *10)
for stock in my_stocks.items():
    print(stock)
    print(stock[0],"has",stock[1])
print("=" *10)
for stock,price in my_stocks.items():
    print(stock,"has",price)
print("=" *10)
my_stocks.pop("SBI") #when we give POP we need specify the KEY value
my_stocks.popitem() #when we give popitem no need to give any argiments
del my_stocks["TCS"] # delete the keys with value
print(my_stocks)
print("=" *10)
swapped = {}
for key,value in my_stocks.items():
    swapped[value] = key
print(swapped)
print("=" *10)
