from student_management_system import StudentManagementSystem


def show_menu():
    print("""
===== Student Management System =====

1. View All Students
2. Search Student
3. Add Student
4. Update Student
5. Remove Student
6. View All Courses
7. Add Course
8. Remove Course
9. Enroll Student in Course
10. Remove Student from Course
11. View Student's Courses
12. Add/Update Grade
13. Show Course Average
14. Exit
""")


def main():
    student_management_system = StudentManagementSystem()

    try:
        while True:
            show_menu()
            user_choice = input("Enter your choice: ").strip()

            if user_choice == "1":
                student_management_system.handle_view_students()

            elif user_choice == "2":
                student_management_system.handle_search_student()

            elif user_choice == "3":
                student_management_system.handle_add_student()

            elif user_choice == "4":
                student_management_system.handle_update_student()

            elif user_choice == "5":
                student_management_system.handle_delete_student()

            elif user_choice == "6":
                student_management_system.handle_view_courses()

            elif user_choice == "7":
                student_management_system.handle_add_course()

            elif user_choice == "8":
                student_management_system.handle_delete_course()

            elif user_choice == "9":
                student_management_system.handle_enroll_course()

            elif user_choice == "10":
                student_management_system.handle_remove_student_from_course()

            elif user_choice == "11":
                student_management_system.handle_view_student_courses()

            elif user_choice == "12":
                student_management_system.handle_add_grade()

            elif user_choice == "13":
                student_management_system.handle_avg_grade_class()

            elif user_choice == "14":
                print("Thank you for using this program.")
                break

            else:
                print("Please enter a valid choice (1-14).")

    finally:
        student_management_system.close()


if __name__ == "__main__":
    main()