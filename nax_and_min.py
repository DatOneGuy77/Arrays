"""
Erick Gonzalez Cruz 
Date: 7/18/2025
File: Finding the Max and Min value in an array!
"""

#Find the max value of an array, now lets also make a funtion for this:
list_2 = [5, 20, 45, 11, 94]

def max_value(any_list):
    max_val = max(any_list)
    return max_val

print(max_value(list_2))
print("-" * 100)

#Now lets create a function with this: 
list_3 = [8, 10, 492, 321, 45, 78, 97]

def min_value(any_list):
    min_val = min(any_list)
    return min_val

print(min_value(list_3))
print('-' * 100)

list_1 = [24, 59, 93, 20, 43]
print(list_1)
print(min_value(list_1))
print(max_value(list_1))
     