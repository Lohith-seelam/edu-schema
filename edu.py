import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Function to establish database connection
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Lohith@123",
            database="EduSchema"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Function to add a new course
def add_course(course_name, description, instructor_id, start_date, end_date):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Courses (course_name, description, instructor_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s)"
            data = (course_name, description, instructor_id, start_date, end_date)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Course added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error adding course: {err}")
    finally:
        if connection:
            connection.close()

# Function to update a course
def update_course(course_id, course_name, description, instructor_id, start_date, end_date):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "UPDATE Courses SET course_name=%s, description=%s, instructor_id=%s, start_date=%s, end_date=%s WHERE course_id=%s"
            data = (course_name, description, instructor_id, start_date, end_date, course_id)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Course updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error updating course: {err}")
    finally:
        if connection:
            connection.close()

# Function to remove a course
def remove_course(course_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "DELETE FROM Courses WHERE course_id = %s"
            data = (course_id,)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Course removed successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error removing course: {err}")
    finally:
        if connection:
            connection.close()

# Function to add a new instructor
def add_instructor(instructor_name, email, bio):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Instructors (instructor_name, email, bio) VALUES (%s, %s, %s)"
            data = (instructor_name, email, bio)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Instructor added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error adding instructor: {err}")
    finally:
        if connection:
            connection.close()

# Function to update an instructor
def update_instructor(instructor_id, instructor_name, email, bio):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "UPDATE Instructors SET instructor_name=%s, email=%s, bio=%s WHERE instructor_id=%s"
            data = (instructor_name, email, bio, instructor_id)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Instructor updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error updating instructor: {err}")
    finally:
        if connection:
            connection.close()

# Function to remove an instructor
def remove_instructor(instructor_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "DELETE FROM Instructors WHERE instructor_id = %s"
            data = (instructor_id,)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Instructor removed successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error removing instructor: {err}")
    finally:
        if connection:
            connection.close()

# Function to add a new student
def add_student(student_name, email, date_of_birth):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Students (student_name, email, date_of_birth) VALUES (%s, %s, %s)"
            data = (student_name, email, date_of_birth)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Student added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error adding student: {err}")
    finally:
        if connection:
            connection.close()

# Function to update a student
def update_student(student_id, student_name, email, date_of_birth):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "UPDATE Students SET student_name=%s, email=%s, date_of_birth=%s WHERE student_id=%s"
            data = (student_name, email, date_of_birth, student_id)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Student updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error updating student: {err}")
    finally:
        if connection:
            connection.close()

# Function to remove a student
def remove_student(student_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "DELETE FROM Students WHERE student_id = %s"
            data = (student_id,)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Student removed successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error removing student: {err}")
    finally:
        if connection:
            connection.close()

# Function to enroll a student in a course
def enroll_student(student_id, course_id, enrollment_date):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (%s, %s, %s)"
            data = (student_id, course_id, enrollment_date)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Student enrolled successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error enrolling student: {err}")
    finally:
        if connection:
            connection.close()

# Function to add a new assessment
def add_assessment(course_id, assessment_name, due_date, total_marks):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Assessments (course_id, assessment_name, due_date, total_marks) VALUES (%s, %s, %s, %s)"
            data = (course_id, assessment_name, due_date, total_marks)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Assessment added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error adding assessment: {err}")
    finally:
        if connection:
            connection.close()

# Function to input grades for a student in an assessment
def input_grade(assessment_id, student_id, marks_obtained, grade):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Grades (assessment_id, student_id, marks_obtained, grade) VALUES (%s, %s, %s, %s)"
            data = (assessment_id, student_id, marks_obtained, grade)
            cursor.execute(sql, data)
            connection.commit()
            messagebox.showinfo("Success", "Grade input successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error inputting grade: {err}")
    finally:
        if connection:
            connection.close()

# Tkinter GUI Application
class EduSchemaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EduSchema Application")

        # Create labels and entry fields for adding/updating courses
        tk.Label(self.root, text="Course Name:").grid(row=0, column=0, padx=10, pady=5)
        self.course_name_entry = tk.Entry(self.root)
        self.course_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Description:").grid(row=1, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Instructor ID:").grid(row=2, column=0, padx=10, pady=5)
        self.instructor_id_entry = tk.Entry(self.root)
        self.instructor_id_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Start Date:").grid(row=3, column=0, padx=10, pady=5)
        self.start_date_entry = tk.Entry(self.root)
        self.start_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="End Date:").grid(row=4, column=0, padx=10, pady=5)
        self.end_date_entry = tk.Entry(self.root)
        self.end_date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons for courses
        tk.Button(self.root, text="Add Course", command=self.add_course).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Update Course", command=self.update_course).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Remove Course", command=self.remove_course).grid(row=5, column=2, padx=10, pady=10)

        # Create labels and entry fields for adding/updating instructors
        tk.Label(self.root, text="Instructor Name:").grid(row=6, column=0, padx=10, pady=5)
        self.instructor_name_entry = tk.Entry(self.root)
        self.instructor_name_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=7, column=0, padx=10, pady=5)
        self.instructor_email_entry = tk.Entry(self.root)
        self.instructor_email_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Bio:").grid(row=8, column=0, padx=10, pady=5)
        self.instructor_bio_entry = tk.Entry(self.root)
        self.instructor_bio_entry.grid(row=8, column=1, padx=10, pady=5)

        # Buttons for instructors
        tk.Button(self.root, text="Add Instructor", command=self.add_instructor).grid(row=9, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Update Instructor", command=self.update_instructor).grid(row=9, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Remove Instructor", command=self.remove_instructor).grid(row=9, column=2, padx=10, pady=10)

        # Create labels and entry fields for adding/updating students
        tk.Label(self.root, text="Student Name:").grid(row=10, column=0, padx=10, pady=5)
        self.student_name_entry = tk.Entry(self.root)
        self.student_name_entry.grid(row=10, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=11, column=0, padx=10, pady=5)
        self.student_email_entry = tk.Entry(self.root)
        self.student_email_entry.grid(row=11, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Date of Birth:").grid(row=12, column=0, padx=10, pady=5)
        self.student_dob_entry = tk.Entry(self.root)
        self.student_dob_entry.grid(row=12, column=1, padx=10, pady=5)

        # Buttons for students
        tk.Button(self.root, text="Add Student", command=self.add_student).grid(row=13, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Update Student", command=self.update_student).grid(row=13, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Remove Student", command=self.remove_student).grid(row=13, column=2, padx=10, pady=10)

        # Create labels and entry fields for enrolling students
        tk.Label(self.root, text="Student ID:").grid(row=14, column=0, padx=10, pady=5)
        self.student_id_entry = tk.Entry(self.root)
        self.student_id_entry.grid(row=14, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Course ID:").grid(row=15, column=0, padx=10, pady=5)
        self.course_id_entry = tk.Entry(self.root)
        self.course_id_entry.grid(row=15, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Enrollment Date:").grid(row=16, column=0, padx=10, pady=5)
        self.enrollment_date_entry = tk.Entry(self.root)
        self.enrollment_date_entry.grid(row=16, column=1, padx=10, pady=5)

        # Button for enrolling students
        tk.Button(self.root, text="Enroll Student", command=self.enroll_student).grid(row=17, column=0, padx=10, pady=10)

        # Create labels and entry fields for adding/updating assessments
        tk.Label(self.root, text="Course ID:").grid(row=18, column=0, padx=10, pady=5)
        self.assessment_course_id_entry = tk.Entry(self.root)
        self.assessment_course_id_entry.grid(row=18, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Assessment Name:").grid(row=19, column=0, padx=10, pady=5)
        self.assessment_name_entry = tk.Entry(self.root)
        self.assessment_name_entry.grid(row=19, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Due Date:").grid(row=20, column=0, padx=10, pady=5)
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.grid(row=20, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Total Marks:").grid(row=21, column=0, padx=10, pady=5)
        self.total_marks_entry = tk.Entry(self.root)
        self.total_marks_entry.grid(row=21, column=1, padx=10, pady=5)

        # Button for adding assessments
        tk.Button(self.root, text="Add Assessment", command=self.add_assessment).grid(row=22, column=0, padx=10, pady=10)

        # Create labels and entry fields for inputting grades
        tk.Label(self.root, text="Assessment ID:").grid(row=23, column=0, padx=10, pady=5)
        self.grade_assessment_id_entry = tk.Entry(self.root)
        self.grade_assessment_id_entry.grid(row=23, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Student ID:").grid(row=24, column=0, padx=10, pady=5)
        self.grade_student_id_entry = tk.Entry(self.root)
        self.grade_student_id_entry.grid(row=24, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Marks Obtained:").grid(row=25, column=0, padx=10, pady=5)
        self.marks_obtained_entry = tk.Entry(self.root)
        self.marks_obtained_entry.grid(row=25, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Grade:").grid(row=26, column=0, padx=10, pady=5)
        self.grade_entry = tk.Entry(self.root)
        self.grade_entry.grid(row=26, column=1, padx=10, pady=5)

        # Button for inputting grades
        tk.Button(self.root, text="Input Grade", command=self.input_grade).grid(row=27, column=0, padx=10, pady=10)

    def add_course(self):
        course_name = self.course_name_entry.get()
        description = self.description_entry.get()
        instructor_id = int(self.instructor_id_entry.get())
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        add_course(course_name, description, instructor_id, start_date, end_date)

    def update_course(self):
        course_id = int(self.course_id_entry.get())
        course_name = self.course_name_entry.get()
        description = self.description_entry.get()
        instructor_id = int(self.instructor_id_entry.get())
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        update_course(course_id, course_name, description, instructor_id, start_date, end_date)

    def remove_course(self):
        course_id = int(self.course_id_entry.get())
        remove_course(course_id)

    def add_instructor(self):
        instructor_name = self.instructor_name_entry.get()
        email = self.instructor_email_entry.get()
        bio = self.instructor_bio_entry.get()
        add_instructor(instructor_name, email, bio)

    def update_instructor(self):
        instructor_id = int(self.instructor_id_entry.get())
        instructor_name = self.instructor_name_entry.get()
        email = self.instructor_email_entry.get()
        bio = self.instructor_bio_entry.get()
        update_instructor(instructor_id, instructor_name, email, bio)

    def remove_instructor(self):
        instructor_id = int(self.instructor_id_entry.get())
        remove_instructor(instructor_id)

    def add_student(self):
        student_name = self.student_name_entry.get()
        email = self.student_email_entry.get()
        date_of_birth = self.student_dob_entry.get()
        add_student(student_name, email, date_of_birth)

    def update_student(self):
        student_id = int(self.student_id_entry.get())
        student_name = self.student_name_entry.get()
        email = self.student_email_entry.get()
        date_of_birth = self.student_dob_entry.get()
        update_student(student_id, student_name, email, date_of_birth)

    def remove_student(self):
        student_id = int(self.student_id_entry.get())
        remove_student(student_id)

    def enroll_student(self):
        student_id = int(self.student_id_entry.get())
        course_id = int(self.course_id_entry.get())
        enrollment_date = self.enrollment_date_entry.get()
        enroll_student(student_id, course_id, enrollment_date)

    def add_assessment(self):
        course_id = int(self.assessment_course_id_entry.get())
        assessment_name = self.assessment_name_entry.get()
        due_date = self.due_date_entry.get()
        total_marks = int(self.total_marks_entry.get())
        add_assessment(course_id, assessment_name, due_date, total_marks)

    def input_grade(self):
        assessment_id = int(self.grade_assessment_id_entry.get())
        student_id = int(self.grade_student_id_entry.get())
        marks_obtained = float(self.marks_obtained_entry.get())
        grade = self.grade_entry.get()
        input_grade(assessment_id, student_id, marks_obtained, grade)


if __name__ == "__main__":
    root = tk.Tk()
    app = EduSchemaApp(root)
    root.mainloop()
