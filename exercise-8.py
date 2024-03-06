'''
Perform the exercises in PART B using Pandas
8. Working with a Series
a. Create a series using list and dictionary.
b. Create a series using NumPy functions in Pandas.
c. Print the index and values of series.
d. Print the first and last few rows from the series.
'''
import pandas as pd
import numpy as np

list=['mathew',201415,23,'computer']
dict={'name':'mathew',
      'age':23,
      'regno':201415,
      'dept':'computer'}
s1=pd.Series(list)
s2=pd.Series(dict)
print(s1)
print(s2)
print("Creating a series using numpy function")
a4=pd.Series(np.arange(11))
print(a4)
print("------------------")
a5=pd.Series(np.zeros(4))
print(a5)
print("printing index and value of series")
l=[64,54,74,26,73,83,26,95,82,71]
s3=pd.Series(l,index=['A','B','C','D','E','F','G','H','N','M'])
print(s3)

print("First 3 values and last 3 values")
print(s3.head(3))
print("---------------------------------------")
print(s3.tail(3))