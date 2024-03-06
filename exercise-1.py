'''
Perform the exercises in PART A using NumPy
1. Basic data structures in NumPy
a. Create a List, set, tuple and dictionary which stores the details of a student (
rollno, name , dept, branch, percentage of mark) in Python and print the
values.
b. Convert the list and tuple as NumPy array.
'''
import numpy as np
#list
l=['mathew',201415,'computer',50]
print("list=",l)
l.reverse()
print("reverse formation of list=",l)
print("length of list=",len(l))
a=np.array(l)
print("numpy list=",a)
print("numpy array Dimension=",np.ndim(a))
#tuple
tup=('mathew',201415,'computer',50)
print("Tuple =",tup)
print("Length of the tuple=",len(tup))
a1=np.array(tup)
print('numpy array tuple=',a1)
print("Dimension=",np.ndim(a1))
print("Dimension=",np.shape(a1))
print("Dimension=",np.size(a1))
#set
set= {'mathew', 201415, 'computer', 50}
print("set =",set)
print("Length of the set=",set)
set.remove(201415)
print("After removing a Element=",set)
set.add(201421)
print("after adding a new element=",set)
#dictionary
dict={'name':'mathew','regno':201415,'dept':'computer','percentage':55}
print(dict)
print("length of dictionary=",len(dict))
print('key in the dictionary=',dict.keys())
print('values in the dictionary=',dict.values())


