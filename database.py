import sqlite3

from course import Course
from student import Student


class DatabaseManager:
    def __init__(self, database_name="Management.db"):
        self.connection = sqlite3.connect(database_name)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

        self.create_table_students()
        self.create_table_courses()
        self.create_table_enrollments()

    # --------------------------------------------------
    # TABLE CREATION METHODS
    # --------------------------------------------------

    def create_table_students(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK (age > 0),
                email TEXT UNIQUE NOT NULL
            )
        """)

        self.connection.commit()

    def create_table_courses(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                course_code TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                max_students INTEGER NOT NULL
                CHECK (max_students > 0)
            )
        """)

        self.connection.commit()

    def create_table_enrollments(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER NOT NULL,
                course_code TEXT NOT NULL,
                grade REAL CHECK (
                grade IS NULL
                OR grade BETWEEN 0 AND 10
                ),

                FOREIGN KEY (student_id)
                    REFERENCES students(id),

                FOREIGN KEY (course_code)
                    REFERENCES courses(course_code),

                PRIMARY KEY (student_id, course_code)
            )
        """)

        self.connection.commit()
    # --------------------------------------------------
    # STUDENT METHODS
    # --------------------------------------------------

    def add_student(self, student):
        sql = """
            INSERT INTO students (
                first_name,
                last_name,
                age,
                email
            )
            VALUES (?, ?, ?, ?)
        """

        values = (
            student.first_name,
            student.last_name,
            student.age,
            student.email
        )

        try:
            self.cursor.execute(sql, values)
            self.connection.commit()

            student.student_id = self.cursor.lastrowid
            return True

        except sqlite3.IntegrityError:
            return False

    def get_all_students(self):
        sql = "SELECT * FROM students"

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        students = []

        for row in rows:
            student = Student(
                first_name=row[1],
                last_name=row[2],
                age=row[3],
                email=row[4],
                student_id=row[0]
            )

            students.append(student)

        return students

    def get_student_by_id(self, student_id):
        sql = "SELECT * FROM students WHERE id = ?"

        self.cursor.execute(sql, (student_id,))
        row = self.cursor.fetchone()

        if row is None:
            return None

        return Student(
            first_name=row[1],
            last_name=row[2],
            age=row[3],
            email=row[4],
            student_id=row[0]
        )

    def update_student(self, student):
        sql = """
            UPDATE students
            SET first_name = ?,
                last_name = ?,
                age = ?,
                email = ?
            WHERE id = ?
        """

        values = (
            student.first_name,
            student.last_name,
            student.age,
            student.email,
            student.student_id
        )

        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def delete_student(self, student_id):
        sql = "DELETE FROM students WHERE id = ?"

        self.cursor.execute(sql, (student_id,))
        self.connection.commit()

    def has_enrollments(self, student_id):
        sql = """
            SELECT *
            FROM enrollments
            WHERE student_id = ?
        """

        self.cursor.execute(sql, (student_id,))

        return self.cursor.fetchone() is not None

    # --------------------------------------------------
    # COURSE METHODS
    # --------------------------------------------------

    def add_course(self, course):
        sql = """
            INSERT INTO courses(course_code,title,max_students)
            VALUES (?, ?, ?)
        """

        values = (
            course.course_code,
            course.title,
            course.max_students
        )

        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def get_all_courses(self):
        sql = "SELECT * FROM courses"

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        courses = []

        for row in rows:
            course = Course(
                row[0],
                row[1],
                row[2]
            )

            courses.append(course)

        return courses

    def get_course_by_code(self, course_code):
        sql = """
            SELECT *
            FROM courses
            WHERE course_code = ?
        """

        self.cursor.execute(sql, (course_code,))
        row = self.cursor.fetchone()

        if row is None:
            return None

        return Course(
            row[0],
            row[1],
            row[2]
        )

    def delete_course(self, course_code):
        sql = """
            DELETE FROM courses
            WHERE course_code = ?
        """

        self.cursor.execute(sql, (course_code,))
        self.connection.commit()

    def has_students_enrolled(self, course_code):
        sql = """
            SELECT *
            FROM enrollments
            WHERE course_code = ?
        """

        self.cursor.execute(sql, (course_code,))

        return self.cursor.fetchone() is not None

    def count_course_students(self, course_code):
        sql = """
            SELECT COUNT(*)
            FROM enrollments
            WHERE course_code = ?
        """

        self.cursor.execute(sql, (course_code,))
        row = self.cursor.fetchone()

        return row[0]

    # --------------------------------------------------
    # ENROLLMENT METHODS
    # --------------------------------------------------

    def add_enrollment(self, student_id, course_code):
        sql = """
        INSERT INTO enrollments (student_id,course_code,grade)
        VALUES (?, ?, NULL)
        """

        values = (
            student_id,
            course_code
        )

        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def remove_student_from_course(
        self,
        student_id,
        course_code
    ):
        sql = """
            DELETE FROM enrollments
            WHERE student_id = ?
            AND course_code = ?
        """

        self.cursor.execute(
            sql,
            (student_id, course_code)
        )

        self.connection.commit()

    def is_student_enrolled(
        self,
        student_id,
        course_code
    ):
        sql = """
            SELECT *
            FROM enrollments
            WHERE student_id = ?
            AND course_code = ?
        """

        self.cursor.execute(
            sql,
            (student_id, course_code)
        )

        return self.cursor.fetchone() is not None

    def view_student_courses(self, student_id):
        sql = """
            SELECT
                courses.course_code,
                courses.title,
                enrollments.grade
            FROM enrollments
            JOIN courses
                ON enrollments.course_code =
                   courses.course_code
            WHERE enrollments.student_id = ?
        """

        self.cursor.execute(sql, (student_id,))

        return self.cursor.fetchall()

    # --------------------------------------------------
    # GRADE METHODS
    # --------------------------------------------------

    def update_grade(
        self,
        student_id,
        course_code,
        grade
    ):
        sql = """
            UPDATE enrollments
            SET grade = ?
            WHERE student_id = ?
            AND course_code = ?
        """

        self.cursor.execute(
            sql,
            (grade, student_id, course_code)
        )

        self.connection.commit()

    def show_avg_grade(self, course_code):
        sql = """
            SELECT AVG(grade)
            FROM enrollments
            WHERE course_code = ?
        """

        self.cursor.execute(sql, (course_code,))
        avg_grade = self.cursor.fetchone()

        return avg_grade[0]

    # --------------------------------------------------
    # CONNECTION METHOD
    # --------------------------------------------------

    def close_connection(self):
        self.connection.close()