'''
13. Consider the Salary dataset, which contains 30 observations consisting of years
of working experience and the annual wage (in dollars).
a. Create a linear plot to identify the relationship between years of working
experience and the annual wages with suitable title , legend and labels.
b. Create a scatter plot to identify the relationship between years of working
experience and the annual wages with title , legend and labels.
c. Also distinguish between observations that have more than 5 years of working
experience and observations that have less than 5 years of working
experience by using different colors in one single plot.
'''

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('salary.csv')
print(df)
eno=df['Eno'].values.tolist()
print("Eno=",eno)
sal=df['salary'].values.tolist()
print("salary=",sal)
plt.plot(eno,sal,label="salary",color='red')
plt.xlabel('Employee No')
plt.ylabel('Salary')
plt.annotate('max salary',xy=(203,75000))
plt.legend()
plt.show()
input("Enter to continue")
plt.xlabel('Employee No')
plt.ylabel('Salary')
exp=df['exp'].values.tolist()
plt.scatter(exp,sal)
plt.show()
input("Enter to continue")
plt.pie(exp,labels=exp)
plt.show()






