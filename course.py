class Course:
    def __init__(self, course_name, course_number, course_section, term_and_year, number_of_students):

        self.course_name = course_name
        self.course_number = course_number
        self.course_section = course_section
        self.term_and_year = term_and_year
        self.number_of_students = number_of_students

# change values of variables
    def change_course_name(self):
        self.course_name = input("Please enter new course name: ")

    def change_course_number(self):
        self.course_number = input("Please enter new course number: ")

    def change_course_section(self):
        self.course_section = input("Please enter new course section: ")

    def change_term_and_year(self):
        self.term_and_year = input("Please enter new course term and year: ")

    def change_number_of_students(self):
        self.number_of_students = input("Please enter new number of students: ")


    # show all attributes
    def print_all(self):
        print("Course info: \n" + self.course_name + "\n" + self.course_number +
              "\n" + self.course_section + "\n" + self.term_and_year +
              "\n" + self.number_of_students + "\n------------")

