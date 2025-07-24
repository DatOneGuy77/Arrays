"""
Erick Gonzalez Cruz
07/23/2025
File: This is a reprt card system using Object oriented proggraming in the data-structure array! 
"""

class Student:
    def __init__(self, student_name):
        self.student_name = student_name

    def student_names(self):
        name_list = ["Erick", "Diego", "Ivan", "Omar", "Isaac"]
        return name_list

    def student_letter_grade(self):
        pass 

class Grade:
    def __init__(self):
        pass 
        
    def student_percentage_grade(self):
        pass
    pass 

if __name__ == "__main__":
    student = Student("name")
    grades = Grade()

    print(student.student_names())

"""
THis should be the layout more or less if possible 
[name, letter Grade, percent grade]

Ex: ["Erick", "A", 100!]
"""

"""
step 1: 
TO start lets just get a list of names, like consisting of 5 people!"
"""