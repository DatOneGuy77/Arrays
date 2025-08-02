"""
Erick Gonzalez Cruz 
7/26/2025
File: Working with an actual array
"""

import numpy as np 

"""Using Addition in Arrays"""
# my_array = np.array([50, 100, 200, 400, 800, 1600])
# my_array_2 = np.array([30, 90, 140, 293, 324, 743])

# addition = my_array + my_array_2

# print(addition)
# #Output: [ 80 190 340 693 1124 2343]

#-----------------------------------------------------------------------------------
"""Finding the minimum and maxium value in an array"""
# array1 = np.array([1, 2, 3, 4, 5])

# min = np.min(array1)
# print(min)
# #Output: 1

# max = np.max(array1)
# print(max)
# #Output: 5

#-----------------------------------------------------------------------------------
"""Sorting the array in order so (1, 2, 3) to (3, 2, 1) and vice versa!"""
# array1 = np.array([8, 3, 5, 1, 6, 2, 4, 7])

# sorting = np.sort(array1) #1-8
# print(sorting) 
# #Output [1 2 3 4 5 6 7 8]

# #Now reversing the list to 8-1
# reversed_array = np.flip(sorting)
# print(reversed_array)
# Output: [8 7 6 5 4 3 2 1]

#-----------------------------------------------------------------------------------
"""Finding the mean and median value in an array!"""
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
"""Multiplying the matricies"""
matrix1 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
matrix2 = np.array([[7.7, 8.8], [9.9, 10.10], [11.11, 12.12]])

result = np.dot(matrix1, matrix2)
print(result)

#Output: 
#[[ 66.913   71.896 ]
#[161.656 174.262]]

#-----------------------------------------------------------------------------------
"""Transpose the matrix"""
# matrix = np.array ([[1, 2, 3], [4, 5, 6]])

# transposed_matrix = np.transpose(matrix)
# print(transposed_matrix)

# #Output:
# #[[1 4]
# # [2 5]
# # [3 6]]