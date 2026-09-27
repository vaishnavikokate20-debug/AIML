#df["column name"].maen()
import pandas as pd
data={
    "name":['Arun','Karun','Varun'],
    "age":[28,34,22],
    "Salary":[1000,2000,3000]

}
df=pd.DataFrame(data)
avg_salary=df['Salary'].mean()
print(avg_salary)