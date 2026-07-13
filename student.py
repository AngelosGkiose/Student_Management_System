class Student:
    def __init__(self, first_name,last_name,age,email,student_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.student_id = student_id

    def __str__(self):
        return (
            f"ID: {self.student_id} | "
            f"Name: {self.first_name} {self.last_name} | "
            f"Age: {self.age} | "
            f"Email: {self.email}  "
        )
