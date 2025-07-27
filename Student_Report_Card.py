"""
Erick Gonzalez Cruz
07/23/2025
File: This is a reprt card system using Object oriented proggraming in the data-structure array! (sort-of) 
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

        return letter_grade, f'{percentage}%' #Ex: [B, 87%]

    def all_list(self):
        names = self.student_names() #We get all the names contained in the list
        full_report = [] #New empty list

        for name in names: #This just means for every (item in this case name) in the list we
            letter, percent = self.student_letter_grade() #Get [grade_list, pecentage] in a variable 
            full_report.append([name, letter, percent]) # return to the empty list and everything into one single list called full_report
            
        return full_report
    
class Classes:
    def __init__(self):
        pass

    def Subjects(self):
        list_1 = ["Math", "English", "Creative Writing", "History", "Art"]
        return list_1

    def multiple_list(self):
        subjects_list = self.Subjects()
        instance_of_Student = Student("name")

        classes = [] #empty list to stro everything (specifically to add every class!!)

        for subjects in subjects_list: #For every subject in subject list
            classes.append([subjects, instance_of_Student.all_list()]) #adding every subject into the students report card

        return [print(item) for item in classes] #With every Subject for every persons report card we print a new line per subject
    
if __name__ == "__main__":
    student = Student("name")
    class_schedule = Classes()

    # print(student.all_list())
    print(class_schedule.multiple_list())

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