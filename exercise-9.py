'''
9. Working with Data Frame Columns
a. Create and print a DataFrame.
b. Find the descriptive statistics for each column.
c. Group the data by the values in a specified column, values in the index.
d. Set Index and columns in a DataFrame.
e. Rename columns and drop columns
f. Select or filter rows based on values in columns.
g. Select single and multiple columns with specific names
'''
import pandas as pd
d1={'name':['mathew','praveen','kalki','vignesh'],
    'age':[18,22,10,25],
    'regno':[201415,201421,201410,201440],
    'percentage':[40,92,32,95]
    }

df=pd.DataFrame(d1)
print(df)
print("Descriptive analysis")
print(df.describe())
print("Group the values by name")
group=df.groupby('name')
for name in group:
    print(name)
print("Setting name as a index")
set_idx=df.set_index('name')
print(set_idx)

df.rename(columns={'name':'name23'},inplace=True)
print("After name modified=",df)
a=df.drop(['name23'],axis=1)
print(a)

print(df['percentage'])
a3=df['percentage']>75
print(a3)

print("single column")
a6=df[df.columns[0:1]]
print(a6)

print("Multiple column")
i=int(input("Enter a element "))
a7=df[df.columns[0:i]]
print(a7)







