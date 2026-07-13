#  Student Management System

A command-line **Student Management System** built with **Python**, **Object-Oriented Programming (OOP)** and **SQLite**.

This project allows users to manage students, courses, enrollments and grades while practicing database design, SQL queries and clean object-oriented programming principles.

---

# Features

###  Student Management
- Add a student
- View all students
- Search student by ID
- Update student information
- Delete a student

###  Course Management
- Add a course
- View all courses
- Delete a course

###  Enrollments
- Enroll a student in a course
- Remove a student from a course
- View all courses for a student

###  Grades
- Add or update a student's grade
- Calculate the average grade for a course

---

# Database

The project uses SQLite with three related tables.

## Students

| Column | Type |
|---------|------|
| id | INTEGER |
| first_name | TEXT |
| last_name | TEXT |
| age | INTEGER |
| email | TEXT |

---

## Courses

| Column | Type |
|---------|------|
| course_code | TEXT |
| title | TEXT |
| max_students | INTEGER |

---

## Enrollments

| Column | Type |
|---------|------|
| student_id | INTEGER |
| course_code | TEXT |
| grade | REAL |

This table creates a many-to-many relationship between students and courses.

---

# Technologies Used

- Python 3
- SQLite
- SQL
- Object-Oriented Programming (OOP)

---

# Concepts Practiced

- Classes and Objects
- Encapsulation
- CRUD Operations
- SQLite Database
- SQL Queries
- Foreign Keys
- Primary Keys
- Composite Primary Keys
- JOIN
- COUNT()
- AVG()
- Input Validation
- Exception Handling
- Modular Programming

---

# Menu

```
===== Student Management System =====

1. View All Students
2. View All Courses
3. Add Student
4. Add Course
5. Enroll Student in Course
6. Remove Student from Course
7. View Student's Courses
8. Add/Update Grade
9. Remove Student
10. Remove Course
11. Show Class Average
12. Exit
```

---

# Sample Output

```
===== Student Management System =====

1. View All Students
2. View All Courses
3. Add Student

Enter your choice: 3

First name: John
Last name: Smith
Age: 20
Email: john@gmail.com

Student added successfully.
```

---

# What I Learned

Through this project I practiced:

- Building a complete CRUD application
- Working with SQLite databases
- Designing relational database tables
- Writing SQL queries
- Using JOIN, COUNT and AVG
- Applying Object-Oriented Programming principles
- Organizing Python projects into multiple classes and files
- Handling user input and validation
- Managing relationships between tables using foreign keys

---

# Future Improvements

- Search students by name
- Search courses by title
- Export data to CSV
- Login system
- GUI version using Tkinter or PyQt
- PostgreSQL support
- Unit tests

---

# Author

Aggelos Trevor
