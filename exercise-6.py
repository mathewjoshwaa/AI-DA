'''
6. Indexing & Sorting in NumPy
a. Load your class Marklist data from a csv file into an array.
b. Access the mark of a student in a particular subject using indexing
techniques.
c. Sort the student details based on Total mark.
d. Select a subset of 2D array using fancy indexing (indexing using integer
arrays)
e. Print student details whose total marks is greater than 250 using Boolean
indexing.
'''
#a
import numpy as np

mark=np.loadtxt('mark3.csv',delimiter=',',dtype=int)
print(mark)

reg=int(input("Enter a index for register no "))
sub=int(input("Enter a index for subject no "))
print('Mark=',mark[reg,sub])

#sorting
a1=mark[np.argsort(mark[:,4])]
print("Before sort")
print(mark)
print("after sort")
print(a1)

#fancy indexing
s1,s2,s3=input("Enter 3 values ").split()
s1=int(s1)
s2=int(s2)
s3=int(s3)
print(mark[[s1,s2,s3]])

#Boolean expression
a5=mark[:,1:4]>75
print(a5)


