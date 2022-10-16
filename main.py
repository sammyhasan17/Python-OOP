from course import Course


def menu():
    print("___________")
    print("[1] Add a course")
    print("[2] Change a course attribute")
    print("[3] Display all course information")
    print("[0] Exit the program")
    print("___________")

array = []

menu()
choice = int(input("Select your choice: "))

# while we don't quit menu, this repeats
while choice != 0:
    if choice == 1:
        # brand new
        course_name = input("Please enter course name: ")
        course_number = input("Please enter course number: ")
        course_section = input("Please enter course section: ")
        term_and_year = input("Please enter term and year: ")
        number_of_students = input("Please enter number of students: ")
        course_object = Course(course_name, course_number, course_section, term_and_year, number_of_students)
        array.append(course_object)

    # Changes a course attribute by user input selecting course and attribute
    elif choice == 2:
        count = 1

        print("These are the courses: ")    # choose the course
        for x in array:
            print(count, end = " ")
            print(x.course_name)
            count = count + 1

        course_choice = int(input("Select the number of the course you would like to change: "))

        #todo print attribute options
        course_attribute = int(input("Which attribute from the course would you like to change?\n"
                                 "1.Course Name \n"
                                 "2.Course number\n"
                                 "3.Course section\n"
                                 "4.Term and Year\n"
                                 "5.Number of Students\n"))
        # calls function  based on course and attribute selection
        if course_attribute == 1:
            array[course_choice-1].change_course_name()

        elif course_attribute == 2:
            array[course_choice - 1].change_course_number()

        elif course_attribute == 3:
            array[course_choice - 1].change_course_section()

        elif course_attribute == 4:
            array[course_choice - 1].change_term_and_year()

        elif course_attribute == 5:
            array[course_choice - 1].change_number_of_students()

        else:
            print("Invalid, try again")
            menu()
            choice = int(input("Select your choice: "))


    elif choice == 3:   # Display all course information
        for x in array:
            print(x.course_name, x.course_number, x.course_section, x.term_and_year, x.number_of_students)

    else:
        print("Invalid choice, please try again")

    menu()
    choice = int(input("Select your choice: "))

print("Goodbye")

#     course_name = input("Please enter course name: ")
#     course_number = input("Please enter course number: ")
#     course_section = input("Please enter course section: ")
#     term_and_year = input("Please enter term and year: ")
#     number_of_students = input("Please enter number of students: ")
#     print("______________")
#
# course1 = Course(course_name, course_number, course_section, term_and_year, number_of_students)


# course1.print_all()
# course1.change_course_name()
# course1.print_all()
# course1.change_course_number()
# course1.print_all()
# course1.change_course_section()
# course1.print_all()
# course1.change_term_and_year()
# course1.print_all()
# course1.change_number_of_students()
# course1.print_all()
