# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:31:09 2023

@author: TARRA NIKHITHA
"""

# NUMPY: stands for numerical python
# fundamental package for numerical computations in python,supports differnet data types
# applications:
    # 1.mathematical and ligical operations on arrays
    #2.fourier transforms
    #3.linear alegbra operations
    #4.random number generation
    
# Array: Ordered Collection of Data types of given length
import numpy as np
a=np.array([2,3,4.5])
print("Array : ",a)

# to get the type 
print(type(a))

# numpy can handle different categorical entities
y=np.array([2,2.4,'n',6])
print(y)

# linspace returns equally spaced numbers within the given range based on the sample number
b=np.linspace(0,10,25,float,retstep=False)
print(b)

# retstep: returns sample as well as step value
c=np.linspace(2,60,10,float,retstep=False)
print(c)


# Generate arrays using arange function
#numpy.arange()- returns equally spaced numbers with in the given range based on step size
d = np.arange(3,16,1.5)
print(d)


# numpy.ones(shape,type)- returns an array of given shape and type filled with ones
e=np.ones((3,4),int)
print(e)


# Generate array using zeroes
# numpy.zeros()- returns an array of given shape and type filled with zero
# numpy.zeros(shape,type),by default type will be float

f=np.zeros((5,4),int)
print(f)

# Generate random.rand to form array
# numpy.random.rand(shape)

g=np.random.rand(6)
print(g)

h=np.random.rand(5,2)
print(h)


# Generate arrays using logspace()
# numpy.logspace()- returns equally spaced numbers based on log scale
# Syntax: numpy.logspace(start,stop,num,endpoint,base,dtype)
# start - start value of the sequence
#• stop - end value of the sequence
#• num - number of samples to generate (default : 50)
#• endpoint- if true, stop is the last sample
#• base - base of the log space (default : 10.0)
#• dtype- type of output arra
 
i=np.logspace(5,10,25,endpoint=True,base=5.0)
print(i)


# Advantages of numpy
#• Numpy supports vectorized operations
#• Array operations are carried out in C and hence the universal functions in numpy are faster than operations carried out on python list

# Advantages of Numpy
# timeit module can be used to measure the execution time for snippets of code
# • Comparing the processing speed of a list and an array using an addition operation

import timeit
# timeit.timeit(stmt, setup, timer, number)
# stmt which is the statement you want to measure; it defaults to ‘pass’.
# setup which is the code that you run before running the stmt; it defaults to ‘pass’. 
# timer which is a timeit.Timer object; it usually has a sensible default value so you don’t have to worry about it.
# the number which is the number of executions you’d like to run the stmt.

print("The time taken is ",timeit.timeit(stmt='x=15;y=15;sum=x+y'))


# time difference between creating array by python list and in numpy 
# in list

print("Time for sum : ",timeit.timeit(stmt='y=(10);t=(5);sum=t+y'))

# in array time

print("Time taken is: ",timeit.timeit(stmt='a=[2,3,4.5]'))


# Advantages of numpy array space
# getsizeof()- returns the size of the object in bytes

# The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to
# the variables and functions that interact strongly with the interpreter.

import sys
l=sys.getsizeof(a)
print(l)

# Note that numpy array uses less bytes for storage than the python list


# numpy.ndarray.itemsize() function return the length of one array element in bytes.
arr = np.array([1, 2, 3, 4], dtype = np.float64)  
g = arr.itemsize  
print (g) 


# numpy.reciprocal() This function returns the reciprocal of argument, element-wise. 
# For elements with absolute values larger than 1, the result is always 0 and for integer 0, overflow warning is issued
m=np.reciprocal(a)
print(m)

# Sorting and searching in numpy
# numpy.where:() It returns the indices of elements in an input array where the given condition is satisfied.
# numpy.where(condition[, x, y]) 

arr = np.array([10, 32, 30, 50, 20, 82, 91, 45])  
i = np.where(arr == 30) 
print("i = ",i)


#  numpy.searchsorted(): The function is used to find the indices into a sorted array arr such that, if elements are inserted before the indices, 
# the order of arr would be still preserved. Here, a binary search is used to find the required insertion indices.   
# numpy.searchsorted(arr, num, side=’left’, sorter=None)

arr = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6] 
print("arr = {}".format(arr)) 
print("Enter element to find: ")
m=int(input())
print("given element in array at index: ",np.searchsorted(arr,m))






                    