import numpy as np
import matplotlib.pyplot as plt

students = ['Student 1', 'Student 2', 'Student 3']
subjects = ['Maths', 'Science', 'English', 'History', 'Geography']
student_data = {}

for student in students:
    print("Enter test scores for" ,student)
    marks = []
    for subject in subjects:
        mark = int(input("Enter the score" ))
        marks.append(mark)
    student_data[student] = marks

for student, marks in student_data.items():
    plt.plot(subjects, marks, marker='x', label=student)

plt.title("Student marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.show()

