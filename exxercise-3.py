'''
3. Built-in functions in NumPy.
a. Load your class Marklist data from a csv (comma separated value) file into
an array. Perform the following operations to inspect your array. Len(), ndim,
size, dtype, shape, info()
b. Apply the aggregate functions on this data and print the results.
(Functions like min(), max(), cumsum(), mean(), median(), corrcoef(),
std())
'''

import numpy as np

mark=np.loadtxt('marks.csv',delimiter=',',dtype=int)
print(mark)
print("Length of the marks=",mark)
print("Dimension=",mark.ndim)
print("Size=",mark.size)
print("shape=",mark.shape)
print("data type=",mark.dtype)

print("------Aggregrate function---------")
print("minimum value=",np.min(mark))
print("maximum value=",np.max(mark))
print("Average value=",np.mean(mark))
print("Median value=",np.median(mark))
print("co-efficient value=",np.corrcoef(mark))
print("cummulative marks=",np.cumsum(mark))
print("standard value=",np.std(mark))


