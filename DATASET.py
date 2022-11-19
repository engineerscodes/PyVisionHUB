import pandas as pd
import re

df = pd.read_csv('C:\\Users\\NAVEEN\\Documents\\school.xls')


for i in range(len(df)):
    print(re.sub('[^A-Za-z0-9]+','',str(df.iloc[i,:1])))


print(df)

res= pd.DataFrame()