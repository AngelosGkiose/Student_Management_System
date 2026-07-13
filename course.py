class Course:
    def __init__(self, course_code, title, max_students):
        self.course_code = course_code
        self.title = title
        self.max_students = max_students

    def __str__(self):
        return f"Code: {self.course_code} | Title: {self.title} | Max Students: {self.max_students}"

