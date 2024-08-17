import tkinter as tk
from tkinter import messagebox

class Subject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def __str__(self):
        return f"{self.name}: {self.grades}"

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject):
        self.subjects[subject.name] = subject

    def add_grade(self, subject_name, grade):
        if subject_name in self.subjects:
            self.subjects[subject_name].add_grade(grade)
        else:
            print("Subject not found.")

    def __str__(self):
        subjects_info = ', '.join(str(subject) for subject in self.subjects.values())
        return f"Student: {self.name}, Subjects: [{subjects_info}]"

Students = {}

def add_student():
    name = student_name_entry.get()
    if name in Students:
        messagebox.showerror('Error', 'Student already exists')
    else:
        Students[name] = Student(name)
        messagebox.showinfo("Success", "Student added.")

def add_grade():
    student_name = student_name_entry.get()
    subject_name = subject_name_entry.get()
    try:
        grade = int(grade_entry.get())
        if student_name in Students:
            if 0 <= grade <= 100:
                if subject_name not in Students[student_name].subjects:
                    Students[student_name].add_subject(Subject(subject_name))
                Students[student_name].add_grade(subject_name, grade)
                messagebox.showinfo('Success', 'Grade added')
            else:
                messagebox.showerror('Error', 'Grade must be between 0 and 100.')
        else:
            messagebox.showerror('Error', 'Student not found.')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid grade.")
    subject_name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def save_data():
    filename = filename_entry.get()
    try:
        with open(filename, 'w') as file:
            for student in Students.values():
                file.write(f"{student.name}\n")
                for subject_name, subject in student.subjects.items():
                    grades = ','.join(map(str, subject.grades))
                    file.write(f"{subject_name}:{grades}\n")
        messagebox.showinfo("Success", "Data saved successfully.")
    except IOError as e:
        messagebox.showerror("Error", f"Error: {e}")

def load_data():
    filename = filename_entry.get()
    global Students
    Students = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            current_student = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if ':' not in line:
                    current_student = Student(line)
                    Students[current_student.name] = current_student
                else:
                    subject_name, grades_str = line.split(':')
                    grades = list(map(int, grades_str.split(',')))
                    subject = Subject(subject_name)
                    subject.grades = grades
                    if current_student:
                        current_student.add_subject(subject)
        messagebox.showinfo("Success", "Data loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except IOError as e:
        messagebox.showerror("Error", f"Error reading data from file: {e}")

root = tk.Tk()
root.title('Student Grade Management')
root.geometry('400x300')

tk.Label(root, text="Student Name").grid(row=0, column=0, padx=10, pady=5)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject Name").grid(row=1, column=0, padx=10, pady=5)
subject_name_entry = tk.Entry(root)
subject_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Grade").grid(row=2, column=0, padx=10, pady=5)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Filename").grid(row=3, column=0, padx=10, pady=5)
filename_entry = tk.Entry(root)
filename_entry.grid(row=3, column=1, padx=10, pady=5)

add_student_button = tk.Button(root, text="Add Student", command=add_student)
add_student_button.grid(row=4, column=0, padx=10, pady=5)

add_grade_button = tk.Button(root, text="Add Grade", command=add_grade)
add_grade_button.grid(row=4, column=1, padx=10, pady=5)

save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.grid(row=5, column=0, padx=10, pady=5)

load_button = tk.Button(root, text="Load Data", command=load_data)
load_button.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
