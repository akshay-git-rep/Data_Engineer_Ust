import numpy as np
import pandas as pd

df = pd.read_csv("iris.csv")
print(df)

income_dc = df.columns
#print(income_dc)

#print(df.columns[:2])
#print(income_dc[:2])

#print(df.dtypes)

df.Y2007 = df.Y2007.astype(float)
#print(df.dtypes)

#print("to know total rows and columns:",df.shape)
#print("to know the total rows only:",df.shape[0])
#print("to know the total columns only:",df.shape[1])

#print("to print first 5 rows")
#print(df.head(3))
#print("to print last 5 rows")
#print(df.tail
#print(df[0:6])


u_value = df.Index.unique()
#print(u_value,len(u_value))

#print(pd.crosstab(df.Index,df.State))

#print(df.Index.value_counts(ascending=False))
#print(df.sample(n=10))
#print(df.sample(frac=0.1))
#print(df.State)
#print(df[["State","Index","Y2008"]])

#data = df.iloc[:5,:3]
#print(data)

zodiac = pd.DataFrame(
        {"name":["akshay","amruth","sudhir"],
         "rashi":["kumba","dhanu","makara"]})
#print(zodiac)
#print(zodiac.columns)
#zodiac.columns =["hesaru","ranga"]
#zodiac.rename(columns = {"name" : "custody"}, inplace=True)
#print(zodiac)
#print(df.columns)
#df.columns = df.columns.str.replace('Y',"year")
#print(df.columns)
#print(df.head())
#df.set_index("Index",inplace=True)
#print(df.head())
#df.reset_index(inplace=True)
#print(df.head())


#print(df)
#data = df.drop(['Index','State'],axis=1)
#data = df.drop(['Index'],axis='column')
#print(data)

#data = df.drop(0,axis=0)
#data= df.drop([0,1,2,3],axis=0)
#print(data)

#print(df.sort_values("State",ascending=False))
#print(df.State.sort_values())
#print(df.sort_values(["Index","State"]))

#print(df)
#df["difference"] = df.Y2014 - df.Y2015
#df["difference"] = df.eval("Y2014 - Y2015")
#print(df)

#data = df.assign(ratio = (df.Y2014/df.Y2015))
#print(data)
#print(df.describe())
#print(df.describe(include=['object']))

#print(df.Y2014.mean(),df.Y2014.median())
#print(df.Y2014.agg(["mean","median","min","max"]))
#print(df.loc[:,["Y2014","Y2015"]],max)

#print(df.groupby("Index")[["Y2014","Y2015"]].min())
#print(df.groupby("Index")[["Y2014","Y2015"]].agg(["mean","max","min"]))
#print(df.groupby("Index").agg({"Y2014":["min","max"],"Y2015":"max" }))

#dt = df.groupby("Index",).agg({"Y2014":["min","max"],"Y2015":"min" })
#print(dt)

#dt = df.groupby(["Index","State"]).agg({"Y2014":["min","max"],"Y2015":"mean" })
#print(dt)
#print(df)
#print(df[df.Index=="A"])
#print(df.loc[df.Index=="C"])
#print(df.loc[df.Index=="A",["Index","State"]])
#print(df.loc[(df.Index == "A") & (df.Y2014 > 1500000),:])
#print(df.loc[(df.Index=="A") | (df.Index=="W")])
#print(df.loc[df.Index.isin(["A","W"])])
#print(df.query("Y2014>1500000 & Y2015>100000"))































