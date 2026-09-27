import pandas as pd
data= {
    "Name":['Ram','Shyam','Sita','Geeta','Meta','lita','Khush','Sai'],
    "age":[10,20,30,40,50,60,70,80],
    "Salary":[100,200,300,400,500,600,700,800],
    "performance":[80,87,67,90,76,56,88,99]
}
df=pd.DataFrame(data)

high_salary=df[df['Salary']>400]
print('Employee with salary>400 ')
print(high_salary)

#filtering rows salary>400 and age>30
filtered=df[(df['Salary']>400)&(df['age']>30)]
print(f'Employee list age>30 and salary>300')
print(filtered)


#usinf qr condition
filtered_qr=df[(df['age']>30) | (df['performance']>80)]
print(filtered_qr)