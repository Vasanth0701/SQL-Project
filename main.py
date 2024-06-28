import mysql.connector
from tkinter import *

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhargav00",
    database="college"
)

# Create a cursor object
mycursor = mydb.cursor()

# Function to create tables for course registration
def create_tables():
    # Table for courses
    mycursor.execute("CREATE TABLE IF NOT EXISTS courses (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), code VARCHAR(10), instructor VARCHAR(255), semester VARCHAR(10), credit_hours INT)")

# Function to register a course
def register_course():
    name = name_entry.get()
    code = code_entry.get()
    instructor = instructor_entry.get()
    semester = semester_entry.get()
    credit_hours = int(credit_hours_entry.get())
    sql = "INSERT INTO courses (name, code, instructor, semester, credit_hours) VALUES (%s, %s, %s, %s, %s)"
    val = (name, code, instructor, semester, credit_hours)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Course registered successfully!")

# Function to display course details
def display_course_details():
    mycursor.execute("SELECT * FROM courses")
    course_details = mycursor.fetchall()
    
    # Create a new window to display course details
    display_window = Tk()
    display_window.title("Course Details")

    for i, course in enumerate(course_details):
        course_label = Label(display_window, text=f"Course {i+1}:")
        course_label.pack()
        course_info = f"Name: {course[1]}, Code: {course[2]}, Instructor: {course[3]}, Semester: {course[4]}, Credit Hours: {course[5]}"
        course_info_label = Label(display_window, text=course_info)
        course_info_label.pack()

# GUI
root = Tk()
root.title("Course Registration System")

# Course Registration Interface
name_label = Label(root, text="Course Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

code_label = Label(root, text="Course Code:")
code_label.grid(row=1, column=0)
code_entry = Entry(root)
code_entry.grid(row=1, column=1)

instructor_label = Label(root, text="Instructor:")
instructor_label.grid(row=2, column=0)
instructor_entry = Entry(root)
instructor_entry.grid(row=2, column=1)

semester_label = Label(root, text="Semester:")
semester_label.grid(row=3, column=0)
semester_entry = Entry(root)
semester_entry.grid(row=3, column=1)

credit_hours_label = Label(root, text="Credit Hours:")
credit_hours_label.grid(row=4, column=0)
credit_hours_entry = Entry(root)
credit_hours_entry.grid(row=4, column=1)

register_btn = Button(root, text="Register Course", command=register_course)
register_btn.grid(row=5, columnspan=2)

# Display Course Details Interface
display_btn = Button(root, text="Display Course Details", command=display_course_details)
display_btn.grid(row=6, columnspan=2)

root.mainloop()