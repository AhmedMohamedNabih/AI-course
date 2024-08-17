import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = []
        self.subjects[subject].append(grade)

Students = {}

def add_student():
    name = student_name_entry.get()
    if name in Students:
        messagebox.showerror('Error', 'Student already exists')
    else:
        Students[name] = Student(name)
        messagebox.showinfo( "student added.")

def add_grade():
    student_name = student_name_entry.get()
    subject_name = subject_name_entry.get()
    try:
        grade = int(grade_entry.get())
        if student_name in Students:
            if 0 <= grade <= 100:
                Students[student_name].add_grade(subject_name, grade)
                messagebox.showinfo( 'Grade added ')
            else:
                messagebox.showerror('Error')
        else:
            messagebox.showerror('Error', 'Student not found.')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid grade.")
    subject_name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
root = tk.Tk()
root.title('Student Grade')
root.geometry('300x200')

tk.Label(root, text="Student Name").grid(row=0, column=0, padx=10, pady=5)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject Name").grid(row=1, column=0, padx=10, pady=5)
subject_name_entry = tk.Entry(root)
subject_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Grade").grid(row=2, column=0, padx=10, pady=5)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1, padx=10, pady=5)

add_student_button = tk.Button(root, text="Add Student", command=add_student)
add_student_button.grid(row=3, column=0, padx=10, pady=5)

add_grade_button = tk.Button(root, text="Add Grade", command=add_grade)
add_grade_button.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()