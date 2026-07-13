from course import Course
from database import DatabaseManager
from student import Student


class StudentManagementSystem:
    def __init__(self):
        self.database = DatabaseManager()

    # --------------------------------------------------
    # STUDENT METHODS
    # --------------------------------------------------

    def handle_add_student(self):
        while True:
            first_name = input("First name: ").strip()

            if not first_name:
                print("First name cannot be empty.")
                continue

            last_name = input("Last name: ").strip()

            if not last_name:
                print("Last name cannot be empty.")
                continue

            try:
                age = int(input("Age: "))

                if age <= 0:
                    print("Age must be greater than 0.")
                    continue

            except ValueError:
                print("Age must be an integer.")
                continue

            email = input("Email: ").strip()

            if not email:
                print("Email cannot be empty.")
                continue

            student = Student(
                first_name,
                last_name,
                age,
                email
            )

            success = self.database.add_student(student)

            if success:
                print("Student added successfully.")
                return

            print("A student with this email already exists.")

    def handle_view_students(self):
        students = self.database.get_all_students()

        if not students:
            print("No students found.")
            return

        for student in students:
            print(student)

    def handle_search_student(self):
        while True:
            try:
                student_id = int(
                    input("Search Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                return

            print(student)
            return

    def handle_update_student(self):
        while True:
            try:
                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                return

            print("\nStudent found.")
            print("Current information:")
            print(student)

            print(
                "\nLeave empty to keep "
                "the current value."
            )

            first_name = input(
                f"First name [{student.first_name}]: "
            ).strip()

            last_name = input(
                f"Last name [{student.last_name}]: "
            ).strip()

            age_input = input(
                f"Age [{student.age}]: "
            ).strip()

            email = input(
                f"Email [{student.email}]: "
            ).strip()

            if age_input:
                try:
                    age = int(age_input)

                    if age <= 0:
                        print("Age must be greater than 0.")
                        continue

                except ValueError:
                    print("Age must be an integer.")
                    continue

                student.age = age

            if first_name:
                student.first_name = first_name

            if last_name:
                student.last_name = last_name

            if email:
                student.email = email

            success = self.database.update_student(
                student
            )

            if success:
                print("Student updated successfully.")
                return

            print("A student with this email already exists.")

    def handle_delete_student(self):
        while True:
            try:
                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                return

            if self.database.has_enrollments(
                student_id
            ):
                print(
                    "Cannot remove this student. "
                    "They are still enrolled in courses."
                )
                return

            print("Student found:")
            print(student)

            confirmation = input(
                "Are you sure you want to delete "
                "this student? (yes/no): "
            ).strip().lower()

            if confirmation == "no":
                print("Deletion cancelled.")
                return

            if confirmation != "yes":
                print("Please enter yes or no.")
                continue

            self.database.delete_student(student_id)

            print("Student deleted successfully.")
            return

    # --------------------------------------------------
    # COURSE METHODS
    # --------------------------------------------------

    def handle_add_course(self):
        while True:
            course_code = input(
                "Course code: "
            ).strip().upper()

            if not course_code:
                print("Course code cannot be empty.")
                continue

            course_title = input(
                "Course title: "
            ).strip()

            if not course_title:
                print("Course title cannot be empty.")
                continue

            try:
                course_max_students = int(
                    input("Course max students: ")
                )

                if course_max_students <= 0:
                    print(
                        "Course max students must "
                        "be greater than 0."
                    )
                    continue

            except ValueError:
                print(
                    "Course max students must "
                    "be an integer."
                )
                continue

            course = Course(
                course_code,
                course_title,
                course_max_students
            )

            success = self.database.add_course(course)

            if success:
                print("Course added successfully.")
                return

            print("A course with this code already exists.")

    def handle_view_courses(self):
        courses = self.database.get_all_courses()

        if not courses:
            print("No courses found.")
            return

        for index, course in enumerate(
            courses,
            start=1
        ):
            print(index, course)

    def handle_delete_course(self):
        while True:
            course_code = input(
                "Course code: "
            ).strip().upper()

            if not course_code:
                print("Course code cannot be empty.")
                continue

            course = self.database.get_course_by_code(
                course_code
            )

            if course is None:
                print("Course not found.")
                return

            if self.database.has_students_enrolled(
                course_code
            ):
                print(
                    "Cannot remove this course. "
                    "Students are still enrolled."
                )
                return

            print("Course found:")
            print(course)

            confirmation = input(
                "Are you sure you want to delete "
                "this course? (yes/no): "
            ).strip().lower()

            if confirmation == "no":
                print("Deletion cancelled.")
                return

            if confirmation != "yes":
                print("Please enter yes or no.")
                continue

            self.database.delete_course(course_code)

            print("Course deleted successfully!")
            return

    # --------------------------------------------------
    # ENROLLMENT METHODS
    # --------------------------------------------------

    def handle_enroll_course(self):
        while True:
            course_code = input(
                "Course code: "
            ).strip().upper()

            if not course_code:
                print("Course code cannot be empty.")
                continue

            course = self.database.get_course_by_code(
                course_code
            )

            if course is None:
                print("Course not found.")
                continue

            try:
                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                continue

            count = self.database.count_course_students(
                course_code
            )

            if count >= course.max_students:
                print("This course is full!")
                return

            success = self.database.add_enrollment(
                student.student_id,
                course.course_code
            )

            if success:
                print(
                    "Student enrolled in the course "
                    "successfully."
                )
                return

            print(
                "This student is already enrolled "
                "in this course."
            )

    def handle_remove_student_from_course(self):
        while True:
            try:
                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                continue

            course_code = input(
                "Enter Course Code: "
            ).strip().upper()

            if not course_code:
                print("Course code cannot be empty.")
                continue

            course = self.database.get_course_by_code(
                course_code
            )

            if course is None:
                print("Course not found.")
                continue

            if not self.database.is_student_enrolled(
                student.student_id,
                course.course_code
            ):
                print(
                    "This student is not enrolled "
                    "in this course."
                )
                continue

            self.database.remove_student_from_course(
                student.student_id,
                course.course_code
            )

            print(
                "Student removed from course "
                "successfully."
            )
            return

    def handle_view_student_courses(self):
        while True:
            try:
                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                continue

            enrollments = (
                self.database.view_student_courses(
                    student.student_id
                )
            )

            if not enrollments:
                print(
                    f"{student.first_name} is not "
                    "enrolled in any courses."
                )
                return

            print(
                f"{student.first_name} "
                f"{student.last_name} is enrolled in:"
            )

            for index, (
                course_code,
                title,
                grade
            ) in enumerate(
                enrollments,
                start=1
            ):
                grade_display = (
                    grade
                    if grade is not None
                    else "(not graded yet)"
                )

                print(
                    f"{index}. {course_code} - "
                    f"{title} - "
                    f"Grade: {grade_display}"
                )

            return

    # --------------------------------------------------
    # GRADE METHODS
    # --------------------------------------------------

    def handle_add_grade(self):
        while True:
            try:
                student_id = int(
                    input("Enter Student ID: ")
                )

                if student_id <= 0:
                    print("Student ID must be greater than 0.")
                    continue

            except ValueError:
                print("Student ID must be an integer.")
                continue

            student = self.database.get_student_by_id(
                student_id
            )

            if student is None:
                print("Student not found.")
                continue

            course_code = input(
                "Course code: "
            ).strip().upper()

            if not course_code:
                print("Course code cannot be empty.")
                continue

            course = self.database.get_course_by_code(
                course_code
            )

            if course is None:
                print("Course not found.")
                continue

            if not self.database.is_student_enrolled(
                student.student_id,
                course.course_code
            ):
                print(
                    "This student is not enrolled "
                    "in this course."
                )
                continue

            try:
                grade = float(
                    input("Enter Grade (0-10): ")
                )

            except ValueError:
                print("Grade must be a number.")
                continue

            if not 0 <= grade <= 10:
                print("Grade must be between 0 and 10.")
                continue

            self.database.update_grade(
                student.student_id,
                course.course_code,
                grade
            )

            print("Grade updated successfully!")
            return

    def handle_avg_grade_class(self):
        while True:
            course_code = input(
                "Course code: "
            ).strip().upper()

            if not course_code:
                print("Course code cannot be empty.")
                continue

            course = self.database.get_course_by_code(
                course_code
            )

            if course is None:
                print("Course not found.")
                continue

            avg_grade = self.database.show_avg_grade(
                course.course_code
            )

            if avg_grade is None:
                print(
                    f"{course.course_code} - "
                    "No grades available yet."
                )
            else:
                print(
                    f"{course.course_code} - "
                    f"Average grade: {avg_grade:.2f}"
                )

            return

    # --------------------------------------------------
    # CONNECTION METHOD
    # --------------------------------------------------

    def close(self):
        self.database.close_connection()