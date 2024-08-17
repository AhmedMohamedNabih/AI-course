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

    def remove_grade(self, subject, grade):
        if subject in self.subjects and grade in self.subjects[subject]:
            self.subjects[subject].remove(grade)
        else:
            messagebox.showerror('Error', 'Grade not found.')

    def update_grade(self, subject, old_grade, new_grade):
        if subject in self.subjects and old_grade in self.subjects[subject]:
            self.subjects[subject].remove(old_grade)
            self.subjects[subject].append(new_grade)
        else:
            messagebox.showerror('Error', 'Grade not found.')

Students = {}

def add_student():
    name = student_name_entry.get()
    if name in Students:
        messagebox.showerror('Error', 'Student already exists.')
    else:
        Students[name] = Student(name)
        update_student_list()
        messagebox.showinfo("Info", "Student added.")

def delete_student():
    name = student_name_entry.get()
    if name in Students:
        del Students[name]
        update_student_list()
        messagebox.showinfo("Info", "Student deleted.")
    else:
        messagebox.showerror('Error', 'Student not found.')

def add_grade():
    student_name = student_name_entry.get()
    subject_name = subject_name_entry.get()
    try:
        grade = int(grade_entry.get())
        if student_name in Students:
            if 0 <= grade <= 100:
                Students[student_name].add_grade(subject_name, grade)
                messagebox.showinfo('Info', 'Grade added.')
            else:
                messagebox.showerror('Error', 'Grade must be between 0 and 100.')
        else:
            messagebox.showerror('Error', 'Student not found.')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid grade.")
    subject_name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def update_grade():
    student_name = student_name_entry.get()
    subject_name = subject_name_entry.get()
    try:
        old_grade = int(old_grade_entry.get())
        new_grade = int(new_grade_entry.get())
        if student_name in Students:
            if 0 <= old_grade <= 100 and 0 <= new_grade <= 100:
                Students[student_name].update_grade(subject_name, old_grade, new_grade)
                messagebox.showinfo('Info', 'Grade updated.')
            else:
                messagebox.showerror('Error', 'Grades must be between 0 and 100.')
        else:
            messagebox.showerror('Error', 'Student not found.')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid grades.")
    subject_name_entry.delete(0, tk.END)
    old_grade_entry.delete(0, tk.END)
    new_grade_entry.delete(0, tk.END)

def remove_grade():
    student_name = student_name_entry.get()
    subject_name = subject_name_entry.get()
    try:
        grade = int(grade_remove_entry.get())
        if student_name in Students:
            if 0 <= grade <= 100:
                Students[student_name].remove_grade(subject_name, grade)
                messagebox.showinfo('Info', 'Grade removed.')
            else:
                messagebox.showerror('Error', 'Grade must be between 0 and 100.')
        else:
            messagebox.showerror('Error', 'Student not found.')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid grade.")
    grade_remove_entry.delete(0, tk.END)

def update_student_list():
    student_list.delete(0, tk.END)
    for student in Students:
        student_list.insert(tk.END, student)

root = tk.Tk()
root.title('Student Management')
root.geometry('400x350')

tk.Label(root, text="Student Name").grid(row=0, column=0, padx=10, pady=5)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject Name").grid(row=1, column=0, padx=10, pady=5)
subject_name_entry = tk.Entry(root)
subject_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Grade").grid(row=2, column=0, padx=10, pady=5)
grade_entry = tk.Entry(root)
grade_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Old Grade").grid(row=3, column=0, padx=10, pady=5)
old_grade_entry = tk.Entry(root)
old_grade_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="New Grade").grid(row=4, column=0, padx=10, pady=5)
new_grade_entry = tk.Entry(root)
new_grade_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Remove Grade").grid(row=5, column=0, padx=10, pady=5)
grade_remove_entry = tk.Entry(root)
grade_remove_entry.grid(row=5, column=1, padx=10, pady=5)

add_student_button = tk.Button(root, text="Add Student", command=add_student)
add_student_button.grid(row=6, column=0, padx=10, pady=5)

delete_student_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_student_button.grid(row=6, column=1, padx=10, pady=5)

add_grade_button = tk.Button(root, text="Add Grade", command=add_grade)
add_grade_button.grid(row=7, column=0, padx=10, pady=5)

update_grade_button = tk.Button(root, text="Update Grade", command=update_grade)
update_grade_button.grid(row=7, column=1, padx=10, pady=5)

remove_grade_button = tk.Button(root, text="Remove Grade", command=remove_grade)
remove_grade_button.grid(row=8, column=0, padx=10, pady=5, columnspan=2)

tk.Label(root, text="Students List").grid(row=9, column=0, padx=10, pady=5)
student_list = tk.Listbox(root)
student_list.grid(row=9, column=1, padx=10, pady=5, rowspan=4, sticky=tk.N+tk.S+tk.E+tk.W)

update_student_list()

root.mainloop()
