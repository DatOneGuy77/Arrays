"""
Erick Gonzalez Cruz
7/20/2025
File: I will try and shift the places of a list! 
"""

#Find a way to shift every element in this list to the left!
list_1 = [5, 15, 25, 35, 45]
print(list_1)
# Original: [5, 15, 25, 35, 45]
# Result:   [15, 25, 35, 45, 5]

def shift_left_by_1(any_list):
    start = any_list[0]

    for i in range(1, len(any_list)):
        any_list[i - 1] = any_list[i]

    any_list[-1] = start

    return any_list

print(shift_left_by_1(list_1))

#This time we shift by the right
list_2 = [20, 50, 80 ,90, 100]
# Original: [20, 50, 80 ,90, 100]
# Result:   [100, 20, 50, 80, 90]

print(list_2)

def shift_right_by_1(any_list):
    shifted_list = [any_list[-1]] + any_list[:-1]
    return shifted_list

print(shift_right_by_1(list_2))