# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:45:33 2023

@author: TARRA NIKHITHA
"""
import numpy as np
# Numpy other operations
# Numpy reshaping of array
# reshape()- recasts an array to new shape without changing it’s data

arr=np.arange(start=1,stop=10).reshape(3,3)
print(arr)

arr1=np.arange(start=1,stop=15).reshape(7,2)
print(arr1)


# Numpy is used for array dimensions
# create an array a
# shape()- returns dimensions of an array ; Syntax: array_name.shape
 
print("Dimension of the array: ",arr1.shape)


# Numpy Addition 
# numpy.sum()- returns sum of all array elements or sum of all array elements over a given axis
# Syntax: numpy.sum(array,axis)

# array() - input array; axis() - axis along which sum should be calculated

arr3=np.sum(arr1,axis=0)
print(arr3)


# Calculate overall sum of given array
x=np.sum(arr)
print(x)

# Calculate the sum along the column
y=np.sum(arr,axis=0)
print(y)


# Calculate the sum along the row
z=np.sum(arr,axis=1)
print(z)

# Elementwise addition between two arrays
# numpy.add()- performs elementwise addition between two arrays
# Syntax: numpy.add(array_1,array_2)

arr5=np.arange(start=7,stop=16).reshape(3,3)
arr4=np.add(arr,arr5)
print(arr4)


# Numpy Multiplication
# numpy.multiply()- performs elementwise multiplication between two arrays
# Syntax: numpy.multiply(array_1,array_2)
r=np.multiply(arr,arr5)
print(r)


# Numpy Substraction
# numpy.subtract()-performs elementwise substraction between two arrays
# Syntax: numpy.substract(array_1,array_2)
s=np.subtract(arr,arr5)
print(s)


# Numpy Division
# numpy.divide()-performs elementwise division between two arrays
# Syntax: numpy.divide(array_1,array_2)
t=np.divide(arr,arr5)
print(t)


# Numpy Remainder
# numpy.remainder()-performs elementwise remainder of division
# Syntax: numpy.remainder(array_1,array_2)
u=np.remainder(arr,arr5)
print(u)


# Accessing Components of array using index of array
# slicing:accessing element on given a,b index
print(arr[0,2])

# Extract elements from first column of array 
print(arr[:,0])

# Extract elements the first row of array 
print(arr[0,:])

# Subset of array
# array name_sub gives subset of the given array
arr5_sub=arr5[:2,:2]
print(arr5_sub)

# updation of sub array is done in array
arr5_sub[0,0]=18
print(arr5_sub)

# modifying the sub set will also lead to modification of original array
print(arr5)


# Modifying the array
# numpy.transpose()- permute the dimensions of array
# Syntax: numpy.transpose(array_1,array_2)
t=np.transpose(arr5)
print(t)
      

# append()- adds values at the end of the array
# Syntax: numpy.append(array,axis)
f=np.append(arr,[[20,21,22]],axis=0)
print(f)

# insert()- adds values at a given position and axis in an array
# Syntax: numpy.insert(array,obj,values,axis)
#array - input array
# obj - index position
# values - array of values to be inserted
# axis - axis along which values should be insert
v=np.insert(arr5,2,[[4,5,6]],axis=1)
print(v)
# does not modify the original array

b=np.insert(arr,1,[[49,69,70]],axis=0)
print(b)



# delete()- removes values at a given position and axis in an array
# Syntax: numpy.delete(array,obj,axis)
#◦ array - input array
#◦ obj - indicate array to be removed or it’s position
#◦ axis - axis along which array should be remove
o=np.delete(arr,1,axis=0)
print(o)


 