# I've created this in order 
# to practice using Numpy briefly 

# Python program using 
# Numpy for some basic 
# mathematical operations

import numpy as np

# Creating two arrays of rank 2 (matrices)
x = np.array([[1, 2], [3, 4]])
y = np.array([[6, 7], [2, 8]])

# Creating two arrays of rank 1 (vectors)
a = np.array([3, 5])
b = np.array([4, 6])

# Inner product of Vectors
print(np.dot(a, b), "\n")

# Matrix and Vector product 
print(np.dot(a, x), "\n")

# Matrix and Matrix product
print(np.dot(x, y), "\n")
