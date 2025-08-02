"""
Erick Gonzalez Cruz
08/01/2025
File: Understanding arrays better in an dimensional way!
"""
import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

# print(array[1, 1, 1])
# [depth, row, column]

word = array[0, 1, 1] + array[1, 2, 2] + array[0, 2, 2] + array[0, 0, 2] + array[1, 0, 1]
print(word)