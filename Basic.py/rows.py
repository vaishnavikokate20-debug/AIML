#head() 5 row from the start
#tail() 5 row from the bottom
import pandas as pd
df=pd.read_json(r"C:\Users\HP\Downloads\sample_Data.json")
print('Display 10 rows of first')
print(df.head(10))

print('Display 10 row of last ')
print(df.tail(10))