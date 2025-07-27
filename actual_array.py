"""
Erick Gonzalez Cruz 
7/26/2025
File: Working with an actual array
"""

import numpy as np 

# my_array = np.array([50, 100, 200, 400, 800, 1600])
# my_array_2 = np.array([30, 90, 140, 293, 324, 743])

# addition = my_array + my_array_2

# print(addition)

#-----------------------------------------------------------------------------------

# array1 = np.array([1, 2, 3, 4, 5])

# min = np.min(array1)
# print(min)
# #Output: 1

# max = np.max(array1)
# print(max)
# #Output: 5

#-----------------------------------------------------------------------------------

# array1 = np.array([8, 3, 5, 1, 6, 2, 4, 7])

# sorting = np.sort(array1) #1-8
# print(sorting) 
# #Output [1 2 3 4 5 6 7 8]

# #Now reversing the list to 8-1
# reversed_array = np.flip(sorting)
# print(reversed_array)
# Output: [8 7 6 5 4 3 2 1]

#-----------------------------------------------------------------------------------

# array1 = np.array([1, 2, 3, 4, 5])

# # Mean value 
# mean_value = np.mean(array1)
# print(mean_value)
# #Output: 3.0

# # Median value
# median_value = np.median(array1)
# print(median_value)
# #Output: 3.0

#-----------------------------------------------------------------------------------

matrix1 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
matrix2 = np.array([[7.7, 8.8], [9.9, 10.10], [11.11, 12.12]])

# Multiply the matricies
result = np.dot(matrix1, matrix2)
print(result)

# Output: 
# [[ 66.913   71.896 ]
# [161.656 174.262]]