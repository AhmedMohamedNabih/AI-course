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
            print(" not found.")

    def __str__(self):
        subjects_info = ', '.join(str(subject) for subject in self.subjects.values())
        return f"Student: {self.name}, Subjects: [{subjects_info}]"

def save_to_file(students, filename):
    try:
        with open(filename, 'w') as file:
            for student in students.values():
                file.write(f"{student.name}\n")
                for subject_name, subject in student.subjects.items():
                    grades = ','.join(map(str, subject.grades))
                    file.write(f"{subject_name}:{grades}\n")
        print(filename)
    except IOError as e:
        print(f"Error: {e}")

def load_from_file(filename):
    students = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            current_student = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if not ':' in line:
                    current_student = Student(line)
                    students[current_student.name] = current_student
                else:
                    subject_name, grades_str = line.split(':')
                    grades = list(map(int, grades_str.split(',')))
                    subject = Subject(subject_name)
                    subject.grades = grades
                    if current_student:
                        current_student.add_subject(subject)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError as e:
        print(f"Error reading data from file: {e}")
    return students

def print_menu():
    print("\nMenu:")
    print("1. Add Student")
    print("2. Add Subject and Grade")
    print("3. View Student Grades")
    print("4. Save Data to File")
    print("5. Load Data from File")
    print("6. Exit")

def main():
    students = {}
    while True:
        print_menu()
        choice = input('Choose a number')
        
        if choice == '1':
            try:
                name = input('Enter student name: ')
                if name in students:
                    print("try another one")
                else:
                    students[name] = Student(name)
                    print("added success")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                student_name = input('Enter student name: ')
                if student_name in students:
                    subject_name = input('Enter subject name: ')
                    try:
                        grade = int(input('Enter grade '))
                        if 0 <= grade <= 100:
                            if subject_name not in students[student_name].subjects:
                                students[student_name].add_subject(Subject(subject_name))
                            students[student_name].add_grade(subject_name, grade)
                            print(f"Grade {grade} added to subject '{subject_name}' for student '{student_name}'.")
                        else:
                            print("Error: Grade must be between 0 and 100.")
                    except ValueError:
                        print("Error: Invalid input. Please enter a valid number for the grade.")
                else:
                    print("not found.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                student_name = input('Enter student name: ')
                if student_name in students:
                    print(students[student_name])
                else:
                    print("not found.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                filename = input('Enter filename to save data: ')
                save_to_file(students, filename)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                filename = input('Enter filename to load data from: ')
                students = load_from_file(filename)
                print("Data loaded successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break 

        else:
            print('Invalid choice, please try again.')

if __name__ == "__main__":
    main()
