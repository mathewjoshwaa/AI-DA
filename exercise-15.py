'''
15. Consider the Iris dataset, where observations belong to either one of three iris
flower classes.
a. Visualize the Histogram for each feature (Sepal Length, Sepal Width,petal
Length & petal Width) separately with suitable bin size and color.
b. Plot the histograms for all features using subplots to visualize all histograms in
one single plot. Save the plot as JPEG file.
c. Plot the boxplots for all features next to each other in one single plot
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('iris3.csv')
print(df)
x=np.arange(50)
y1=df['sepal length']
y1=y1[0:50]
y2=df['sepal width']
y2=y2[0:50]
y3=df['petal length']
y3=y3[0:50]
y4=df['petal width']
y4=y4[0:50]
print(y1)
print(y2)
print(y3)
print(y4)
x=df[df.columns[0:4]]
input("Enter to continue")
bin=10
clr=['red','green','blue','yellow']
plt.hist(x,bin,histtype='bar',color=clr,label="colours")
plt.show()
input("Enter to continue")
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,10))
print(fig)
print(axes)
fig.suptitle("Histogram for all features")
axes[0,0].hist(y1,color='red')
axes[0,1].hist(y2,color='blue')
axes[1,0].hist(y3,color='green')
axes[1,1].hist(y4,color='yellow')
axes[0,0].set_title("sepal length")
axes[0,1].set_title("sepal width")
axes[1,0].set_title("petal length")
axes[1,1].set_title("petal width")
plt.show()
input("Enter to continue")
fig,axes=plt.subplots(nrows=4,ncols=2,figsize=(10,10))

axes[0,0].hist(y1,color='red')
y1=df['sepal length']
y1.plot(kind="box",ax=axes[0,1],label="box plot")

axes[1,0].hist(y2,color='green')
y2=df['sepal width']
y2.plot(kind="box",ax=axes[1,1],label="box plot")

axes[2,0].hist(y3,color='blue')
y3=df['petal length']
y3.plot(kind="box",ax=axes[2,1],label="box plot")

axes[3,0].hist(y4,color='yellow')
y4=df['petal width']
y4.plot(kind="box",ax=axes[3,1],label="box plot")
plt.show()


