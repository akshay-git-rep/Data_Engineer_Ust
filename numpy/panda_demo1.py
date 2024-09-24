import pandas as pd
import numpy as np

df = pd.read_csv("income.csv")
#print(df)

#printing oly columns
#print(df.columns)
#print(len(df.columns))

#slicing
income_col = df.columns
#print(df.columns[5:])
# print(income_col[5:])

#data types
#print(df.dtypes)

#change data type
#df.Y2015 = df.Y2015.astype(float)
#print(df.dtypes)

# print("to know total rows and columns:",df.shape)
# print("to know total rows:",df.shape[0])
# print("to know total columns:",df.shape[1])

#print(df.head())
# print(df.iloc[0:5])

#to get unique value from the INDEX column
u_values = df.Index.unique()
#print(u_values)

#link between state and Index, Compare between state and Index
#print(pd.crosstab(df.Index,df.State))

#Finding index count which is repeated
#print(df.Index.value_counts(ascending=False))

#sample - sample give random values, n=3(3 rows), frac=0.1(10% of total data)
# data = df.sample(n=3)
# data1 = df.sample(frac=0.1)
# print(data1)

#print(df.State)
#print(df['State'])
#print(df[["Index","State"]])

# data = df.iloc[0:5,0:3]
# #print(data)
# data = df.loc[0:2,["Index","State"]]
# print(data)

#Creating data frame

data = {
    "name":["akshay","amruth","sudhir","alladin"],
    "Sign":["aquaris","dhanu","kumba","rashi"],
    "age":[25,45,15,35]
}

df2 = pd.DataFrame(data)
# print(df2)
# #sorting rows based on the columns
# data = df2.sort_values(["name","Sign"],ascending=False)
# print(data)

# print(df2.columns)
# df2.columns = ["names","signs"]
# print(df2.columns)

# print(df2)
# df2.rename(columns = {"name":"cust_name"},inplace=True)
# print(df2)

# print(df.columns)
# df.columns = df.columns.str.replace("Y","Year")
# print(df.columns)

#print(df.head())
# df.set_index("Index",inplace=True)
# print(df.head())
# df.reset_index(inplace=True)
# print(df.head())

data = {
    "name":["akshay","amruth","sudhir","alladin"],
    "Sign":["aquaris","dhanu","kumba","rashi"],
    "age":[25,45,15,35],
    "newage":[10,50,20,30]
}
df2 = pd.DataFrame(data)

#Display all the columns where Index value is "A" or "C"
#print(df[df.Index == "A"])
#print(df.loc[df.Index == "C","Y2002"])

#Display particular where condition get satisfied
#print(df.loc[df.Index == "A","State"]) #Display oly state columns where Index value is "A"

#And condition we give in list
#print all the columns where Index C and Y2002 value more than
#print(df.loc[(df.Index == "C") & (df.Y2002 > 1685340)])

#Or condition 
#display where Index value is A or W and display Index and State columns
#print(df.loc[(df.Index == "A") | (df.Index == "W"),["Index","State"]])

#is in Condition
#print(df.loc[df.Index.isin(["A","W"]),["Index","State"]]) #display oly Index and State column
#print(df.loc[(df.Index.isin(["A","W"]))]) #display al the columns

#alternative
#print(df.query("Index == 'A' | Index == 'W'"))

#To give null value we can give np.nan by using numpy
mydata = {
    "items":["TV","fridge","TV","bike"],
    "price":[10,20,10,90]
}

df3 = pd.DataFrame(mydata)

#display diblicate
print(df3)
#we get boolean value if any dublicate found will get true value in the place of dublucate value
#by default keep will having value as first else we can give last. so it consider 1st as dublicate and last as original
#data = df3.duplicated(keep="first")
#print(data)

#another way find dublicate
#data = data.loc[data.duplicated()]
#print(data)

#drop dublicate
#the value will be shown while deleting dublicate
# data = df3.drop_duplicates(keep="last")
# print(data)

#another way 
data = df3.loc[df3.drop_duplicates()]
print(data)
