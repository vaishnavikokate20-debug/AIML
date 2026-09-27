import pandas as pd
data= {
    "Name":['Ram','Shyam','Sita','Geeta','Meta','lita','Khush','Sai'],
    "age":[10,20,30,40,50,60,70,80],
    "Salary":[100,200,300,400,500,600,700,800],
    "performance":[80,87,67,90,76,56,88,99]
}
df=pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print("Names(Single column return series)")
name=df['Name']
print(name)

#selecting multiple columns

subset=df[["Name", "Salary"]]
print('\nSubset with name and salary')
print(subset)