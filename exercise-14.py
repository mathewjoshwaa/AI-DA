'''
14. Consider the Iris dataset, where observations belong to either one of three iris
flower classes.
a. Visualize the average value for each feature of the Setosa iris class using a
bar chart.
Page 159 of 233
b. Format the obtained bar graph by Changing the color of each bar, Change the
Edge color , Linewidth and Line style.
'''

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('iris3.csv')
print(df)
y=df.loc[df['class']=='Iris-setosa'].mean()
x=['sl','sw','pl','pw']
print(x)
print(y)
plt.xlabel("features")
plt.ylabel("Average")
plt.bar(x,y)
plt.show()
input("Enter to continue")
clr=['red','lime','orange','green']
plt.bar(x,y,color=clr)
plt.xlabel("features")
plt.ylabel("Average")
plt.show()
input("Enter to continue")
clr=['red','lime','orange','green']
plt.bar(x,y,fill=False,linestyle='-.',edgecolor=clr,linewidth=2)
plt.show()
