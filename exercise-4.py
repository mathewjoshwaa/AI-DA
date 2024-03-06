'''
4. Handling Multiple Arrays
a. Create two python NumPy arrays (boys, girls) each with the age of n
students in the class.
b. Get the common items between two python NumPy arrays.
c. Get the positions where elements of two arrays match.
d. Remove from one array those items that exist in another.
e. Extract all numbers between a given range from a NumPy array.
'''

import numpy as np
l1=[15,21,16,8,18,14,13,10,20,22]
l2=[22,14,25,9,16,7,20,45,22,45]

b=np.array(l1)
g=np.array(l2)
print("boys=",b)
print("girls=",g)
comm,idx1,idx2=np.intersect1d(b,g,return_indices=True)
print("Common Element in both array=",comm)
print('common element index in boys=',idx1)
print('common element index in girls=',idx2)
a1=np.delete(b,idx1)
a2=np.delete(g,idx2)
print("uncommon element in boys=",a1)
print("uncommon element in girls=",a2)

#extracting range of values
marks=[67,87,98,78,98,97,56,75,86,65]
m=np.array(marks)
p=np.where(np.logical_and(m>=75,m<=100))
print(p)
f=np.where(np.logical_and(m>0,m<75))
print(f)


