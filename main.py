
from student_management_system import StudentManagementSystem


def show_menu():
    print("""===== Student Management System =====

1. View All Students
2. View All Courses
3. Add Student
4. Add Course
5. Enroll Student in Course
6. Remove Student from Course
7. View Student's Courses (with grades)
8. Add/Update Grade
9. Remove Student
10. Remove Course
11. Show Class Average (per course)
12. Exit""")



def main():
    student_management_system = StudentManagementSystem()
    while True:
        show_menu()
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            student_management_system.handle_view_students()
        elif user_choice == "2":
            student_management_system.handle_view_courses()
        elif user_choice == "3":
            student_management_system.handle_add_student()
        elif user_choice == "4":
            student_management_system.handle_add_course()
        elif user_choice == "5":
            student_management_system.handle_enroll_course()
        elif user_choice == "6":
            student_management_system.handle_remove_student_from_course()
        elif user_choice == "7":
            student_management_system.handle_view_student_courses()
        elif user_choice == "8":
            student_management_system.handle_add_grade()
        elif user_choice == "9":
            student_management_system.handle_delete_student()
        elif user_choice == "10":
            student_management_system.handle_delete_course()
        elif user_choice == "11":
            student_management_system.handle_avg_grade_class()
        elif user_choice == "12":
            print("Thank you for using this program ")
            student_management_system.close()
            break
        else:
            print("Please enter a valid choice")



    pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


