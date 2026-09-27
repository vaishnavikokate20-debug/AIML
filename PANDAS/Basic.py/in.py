import pandas as pd 
df=pd.read_json(r"C:\Users\HP\Downloads\sample_Data.json")
print("Displaying the info of data set")
print(df.info())