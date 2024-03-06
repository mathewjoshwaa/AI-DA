'''
a. Slicing DataFrame using loc and iloc.
b. Filter multiple rows using isin.
c. Select first n rows and last n rows
d. Select rows randomly n rows and fractions of rows (use df.sample method)

e. Count the number of rows with each unique value of variables
f. Select nlargest and nsmallest values.
g. Order/sort the rows.
'''

import pandas as pd

df=pd.read_csv("example2.csv")
print(df)
print("using iloc and loc methods")
print(df.loc[0:3])
print("--------------")
print(df.iloc[0:2])
print('using isin method')
df1=df.loc[df['name'].isin(['Albert','John'])]
print(df1)
print("------------------")
print("printing first 5 rows and last 5 rows")
print(df.head(5))
print(df.tail(5))
print("uniq rows in gme_id")
print(df['game_id'].value_counts())
print("largest and smallest values in points")
print(df.nlargest(3,['points']))
print(df.nsmallest(3,['points']))
print("Sorted according name")
print(df.sort_values('name'))




