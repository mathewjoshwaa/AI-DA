'''
12. Merge and combine data
a. Perform the append, concat and combine_first operations on DataFrames.
b. Apply different types of merge on data.
c. Use a query method to filter DataFrame with multiple conditions
'''
import pandas as pd
d={'a':[1,2,3,4],
    'b':[5,6,7,8]
   }
d1={'a':[1,2,3],
    'b':[6,7,8]
   }
df1=pd.DataFrame(d,index=[1,2,3,4])
df2=pd.DataFrame(d1,index=[5,6,7])

print("append")
d2=df1.append(df2)
print(d2)
print("concate")
frame=[df1,df2]
d3=pd.concat(frame)
print(d3)
print("combine_first")
d4=d3.combine_first(df1)
print(d4)
print("Merging the datas")
m1=pd.merge(df1,df2,on='a')
print(m1)
m2=df1.merge(df2,how='right')
print(m2)

d11={"name":['mathew','praveen'],
     'age':[21,15]}
df3=pd.DataFrame(d11)
q1=df3[df3['name']=='mathew']
print(q1)
d8=df3.query("name=='mathew' and age==21")
print(d8)

