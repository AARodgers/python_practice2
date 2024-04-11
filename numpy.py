# Working with Numpy: good to use when you are just working numbers but Panda is good
# with mix of strings and numbers, pandas depends on numpy

pip install numpy

#Import numpy
import numpy as np

# make array
a = np.array([1, 2, 3])
print(a)

# Shape of the array
print(a.shape)  # Output: (3,)

# Data type of the array
print(a.dtype)  # Output: int64
# (3, ) means no columns, it's one dimensional

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Addition
print(a + b)  # Output: [5 7 9]
# Multiplication
print(a * 2)  # Output: [2 4 6]

a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
# reshape into a 2 by 3 charts
print(b)
b.shape

#Square root, returns array of sq root of each index
a = np.array([1, 2, 3])

# Square root
print(np.sqrt(a))

# Broadcasting
a = np.array([1, 2, 3])
b = 2

# Broadcasting
print(a * b)  # Output: [2 4 6]

# Slicing an array
a = np.array([1, 2, 3, 4, 5])
print(a[1:4])  # Output: [2 3 4]

# Importing and Exporting Data
#Importing and Exporting Data
# Save an array to a text file
np.savetxt('array.txt', a)

# Load data from a text file
b = np.loadtxt('array.txt')
