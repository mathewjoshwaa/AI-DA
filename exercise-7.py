'''
7. Handing Two dimensional array in NumPy
a. Import iris dataset with numbers and texts keeping the text intact into python
NumPy.
b. Convert the 1D iris to 2D array (iris2d) by omitting the species text field.
c. Find the number and position of missing values in iris2d's sepal_length
d. Insert np.nan values at 20 random positions in iris 2d dataset
e. Filter the rows of iris2d that has petal_length > 1.5 and sepal_length < 5.0
'''

import numpy as np
import csv

with open('Iris.csv') as file_name:
    content=csv.reader(file_name)
    arr1=list(content)

print(arr1)
arr2=np.reshape(arr1,(150,5))
print(arr2)
arr3=arr2[:,:4]

input("Enter to continue")
arr3=arr3.astype('float64')
n=20
index=np.random.choice(arr3.size,n,replace=False)
arr3.ravel()[index]=np.nan
print(arr3)

input("Enter to continue")
a=np.where(arr3[:1,:2]>1.5)
print(arr3[a])

input("Enter to continue")
b=np.where(arr3[:,0:1]<5.0)
print(arr3[b])
