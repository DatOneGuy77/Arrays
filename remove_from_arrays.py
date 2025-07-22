"""
Erick Gonzalez Cruz
7/20/2025
File: This is to practice removing stuff arrays! Including duplicates, even numbers, and maybe smth else!
"""

#Well to start elts just try removing duplicates!
list_1 = [20, 40, 20, 32, 59, 2]

def remove_dupliates(any_list):
    removed = set(any_list)
    return removed

print(remove_dupliates(list_1))

print("-" * 100)

#We remove duplicates!
def remove_even_num(any_list):
    result = []
    for num in any_list:
        if num % 2:
            result.append(num)
    return result

print(remove_even_num(list_1))