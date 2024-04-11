# Working with Numpy
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
