'''
2. Arrays in NumPy
a. Create arrays using different intrinsic methods (ones, zeros, arange,
linspace, indice) and print their values.
b. Check the results of arithmetic operations like add(), subtract(), multiply()
and divide() with arrays created using arange and ones intrinsic method.
c. Check the results of mathematical operations like exp(), sqrt(), sin(), cos(),
log(), dot() on an array created using arange intrinsic method
'''

import numpy as np
print(np.info())
a1=np.zeros(5)
a2=np.ones(3)
a3=np.arange(10)
a4=np.linspace(2,10)
a5=np.indices((2,3))
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

#arithemetic operation
a=np.ones(6)
k=int(input("Enter a value "))
a=np.add(a,k)
print('Addition=',a)
a=np.subtract(a,k)
print('subtraction=',a)
a=np.multiply(a,k)
print('multiplication=',a)
a=np.divide(a,k)
print('Division=',a)

#mathematical operation
a1=np.linspace(2,10)
print(a1)
print("Exponenet=",np.exp(a1))
print("square root=",np.sqrt(4))
print("sin=",np.sin(a1))
print("cos=",np.cos(a1))
print("log=",np.log(a1))
print("dot=",np.dot(2,3))






