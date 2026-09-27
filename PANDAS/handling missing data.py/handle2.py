import pandas as pd
data= {
    "name":['Ram','Shyam','Sita','Geeta','Meta','lita','Khush','Sai'],
    "age":[10,None,30,40,50,60,70,80],
    "Salary":[100,200,None,400,500,600,700,800],
    "performance":[80,87,67,90,76,56,88,99]
}
df=pd.DataFrame(data)
print(df)
df.fillna(0,inplace=True)
print(df)
df['age'].fillna(df['age'].mean(),inplace=True)
print(df)