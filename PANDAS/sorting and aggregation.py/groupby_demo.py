import pandas as pd
data={
    "name":['Arun','Karun','Varun','marun','narun'],
    "age":[28,34,22,34,28],
    "Salary":[15000,45000,52000,48000,60000]

}
df=pd.DataFrame(data)
grouped=df.groupby("age")["Salary"].sum()
print(grouped)