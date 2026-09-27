#sorting data at one column sort_values()
# df.sort_values(by="Column name",true/false,inplace=true)  
# for asc order = true
# asc order = false  then it is desc
import pandas as pd
data={
    "name":['Arun','Karun','Varun'],
    "age":[28,34,22],
    "Salary":[1000,2000,3000]

}
df=pd.DataFrame(data)
df.sort_values(by=["age","Salary"],ascending=[True,False],inplace=True)
print("Sorted age by descending")
print(df)
