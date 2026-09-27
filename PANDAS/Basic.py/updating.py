import pandas as pd
data= {
    "name":['Ram','Shyam','Sita','Geeta','Meta','lita','Khush','Sai'],
    "age":[10,20,30,40,50,60,70,80],
    "Salary":[100,200,300,400,500,600,700,800],
    "performance":[80,87,67,90,76,56,88,99]
}
df=pd.DataFrame(data)
print(df)
#.loc[] for accsing specific 
# df.loc[row_index,"Column_name"]=new_value
df.loc[1,'Salary']=1000
print(df)
