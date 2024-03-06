'''
5. Array Slicing in NumPy
a. Load your class Marklist data into an array called “marks” to store students
roll_num, subject marks and result.
b. Split all rows and all columns except the last column into an array called
“features”.
c. Split the marks array into 3 equal-sized sub-arrays each for 3 different
subject marks.
d. Split the last column into an array “label”.
e. Delete the roll_num column from the marks array and insert a new
column student name in its place.
'''

import numpy as np

name=np.loadtxt('name.csv',delimiter=',',dtype=str)
mark=np.loadtxt('marks1.csv',delimiter=',',dtype=str)
print(name)
print(mark)

print("splitting all rows and column except last one:")
a1=mark[:,:4]
print(a1)

print('splitting marks alone')
temp=mark[:,1:4]
print(temp)

print("horizontal split of mark")
a3=np.hsplit(temp,3)
print(a3)

print("splitting first column alone")
a4=mark[:,:1]
print(a4)

print("inserting name into marks")
a5=np.insert(temp,0,name,axis=1)
print(a5)







