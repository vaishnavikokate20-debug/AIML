import pandas as pd
data={
    "Name":['Ram','Shyama','Sita'],
     "age":[10,20,30]  ,
     "City":['nagpur','mumbai','delhi']     
            
}

df=pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index=False)