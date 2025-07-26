"""
Erick Gonzalez Cruz
07/23/2025
File: This is a reprt card system using Object oriented proggraming in the data-structure array! 
"""
import random 

class Student:
    def __init__(self, student_name):
        self.student_name = student_name

    def student_names(self): #List of all student names
        name_list = ["Erick", "Diego", "Ivan", "Omar", "Isaac"]
        return name_list

    def student_letter_grade(self):
        grade_list = ["A", "B", "C", "D", "F"] #List containing all letter grades

        percentage = random.randint(50, 100) #Generate number between (50-100)

        if percentage >= 90:
            letter_grade = grade_list[0] #A
        elif percentage >= 80:
            letter_grade = grade_list[1] #B
        elif percentage >= 70:
            letter_grade = grade_list[2] #C
        elif percentage >= 60:
            letter_grade = grade_list[3] #D
        else:
            letter_grade = grade_list[4] #F 

        return letter_grade, f'{percentage}%' #Ex: [Erick, B]

    def all_list(self):
        names = self.student_names() #We get all the names contained in the list
        full_report = [] #New empty list

        for name in names: #This just means for every (item in this case name) in the list we
            letter, percent = self.student_letter_grade() #Get [grade_list, pecentage] in a variable 
            full_report.append([name, letter, percent]) # return to the empty list and everything into one single list called full_report
            
        return full_report

if __name__ == "__main__":
    student = Student("name")

    print(student.all_list())

"""
THis should be the layout more or less if possible 
[name, letter Grade, percent grade]

Ex: ["Erick", "A", 100!]
"""

"""
step 1: 
TO start lets just get a list of names, like consisting of 5 people!"
step 2:
Now get grade list!
step 3; 
use zip
step 4:

"""