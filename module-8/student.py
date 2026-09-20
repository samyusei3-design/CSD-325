#Samuel Guizar
#9/18/26
#Module 8.2 Assignment

#This program works with student information in a json file 

import json

def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} :"f"ID = {student['Student_ID']}, "
             f"Email = {student['Email']}")

#Load students from json file
with open("student.json", "r") as file:
    students = json.load(file)

#Display original student list
print("Original Student List:")
print_students(students)

#Add a new student to the list
students.append({
    "F_Name": "Samuel",
    "L_Name": "Guizar",
    "Student_ID": "59316",
    "Email": "sguizar@my365.bellevue.edu"
})

#Display updated student list
print("\nUpdated Student List:")
print_students(students)

#Save the updated student list to the json file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

#Notify the user that the student list has been updated
print("\nStudent list has been updated and saved to 'student.json'.")

