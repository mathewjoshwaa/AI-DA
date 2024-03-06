'''
11. Handling missing data and duplicates
a. Identify rows with missing data ( isnull(), notnull()) and replace NA/Null data
with a given value.
b. Drop rows and columns with any missing data (dropna(), dropna(1))
c. Find duplicate values and drop duplicates.
d. Fill the missing values using forward filling and backward filling.
e. Replace the missing value with new value and write the dataframe to a CSV
file in the local directory
'''
import pandas as pd
import numpy as np
d={'first score':[56,np.nan,45,87,np.nan,33,87,np.nan,75,54],
   'Second score':[np.nan,98,84,49,89,np.nan,43,28,np.nan,50],
   'Third score':[51,np.nan,34,np.nan,65,49,np.nan,74,47,np.nan]
   }
df=pd.DataFrame(d)
print(df)
print("checking with isnull() and notnull()")
print(df.isnull())
print('------------')
print(df.notnull())
print('droping rows using dropna')
print(df.dropna())
print('------------')
print(df.dropna(axis=1))

dict={'name':['mathew','raj','praveen','raj'],
      'age':[21,15,43,15]
      }
df2=pd.DataFrame(dict)
print(df2)
print("Duplicated values=",df2.duplicated())
print("droping the duplicates",df2.drop_duplicates())
print("using bfilla dn ffill")
print(df.fillna(method='ffill'))
print("----------------------")
print(df.fillna(method='bfill'))
print("replacing the values")
df=df.fillna(value=40)
print(df)
df.to_csv('ex11.csv')





