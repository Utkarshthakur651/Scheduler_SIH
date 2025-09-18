import mysql.connector as msc

myDB = msc.connect(
    host="localhost", user="root", passwd="@B00y@hmysql", database="schedule"
)
crs = myDB.cursor()

branches = {}


class Branch:
    students = []
    courses_s1 = []
    courses_s2 = []

    def __init__(self, name):
        self.name = name

    def addStudent(self):
        student = input("Enter student name: ")
        self.students.append(student)
        print(f"Student {student} added to branch {self.name}")

    def get_commits(self):
        return self.commits


class Faculty:
    def __init__(self, name, fid, dept):
        self.fid = fid
        self.name = name
        self.dept = dept
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)


def mainMenu():
    print("1. Add Branch")
    print("2. Add Faculty")
    print("3. Add Deptartment")
    print("4. Add Student")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        exit()
    elif choice not in [1, 2, 3, 4]:
        print("Invalid choice")
        mainMenu()

    elif choice == 1:
        while True:
            print("\n\t\tBranch Addition Menu\n")
            bid = int(input("Enter Branch ID: "))
            branch_name = input("Enter Branch name: ")
            sem = int(input("Enter semester:"))
            course_str = input(f"Enter courses offered in semester {sem} (comma separated):")
            courses= course_str.split(",")
            if branch_name not in branches:
                branches[branch_name] = Branch(branch_name)
                for course in courses:
                    course = course.strip()
                    if sem == 1:
                        if course not in branches[branch_name].courses_s1:
                            branches[branch_name].courses_s1.append(course)
                            query = f"INSERT INTO branch (bid, bname, bcourses_s1) VALUES (%s, %s, %s)"
                    elif sem == 2:
                        if course not in branches[branch_name].courses_s2:
                            branches[branch_name].courses_s2.append(course)
                            query = f"INSERT INTO branch (bid, bname, bcourses_s2 ) VALUES (%s, %s,%s)"
                    values = (bid, branch_name, course_str)

                crs.execute(query,values )
                myDB.commit()
                
            print(f"Branch {branch_name} added.")
            exit = input("Do you want to add more students? (y/n): ")
            if exit.lower() == "n":
                break

    elif choice == 4:
        while True:
            print("\n\t\tStudent Addition Menu\n")
            branch_name = input("Enter Branch name:")
            if branch_name in branches:
                s_name = input("Enter Student name:")
                branches[branch_name].students.append(s_name)
                query = f"INSERT INTO {branch_name} (sname, scourses) VALUES (%s, %s)"
                values = (s_name, ",".join(Branch.courses))
                crs.execute(query, values)
                myDB.commit()
                print(f"Student {s_name} added to database.\n")
                exit = input("Do you want to add more students? (y/n): ")
                if exit.lower() == "n":
                    break
            else:
                print(
                    f"Branch {branch_name} does not exist. Please add the branch first."
                )

    # elif choice==2:
    #     dept_name = input("Enter Branch name: ")
    #     depts={}
    #     depts[dept_name]=(Branch(dept_name))
    #     print(f"Branch {branch_name} added.")


while True:
    mainMenu()

# while True:
#     course = input("Enter course name (or 'exit' to finish): ")
#     if course.lower() == 'exit':
#         break
#     branch = Branch(course)
#     while True:
#         f_name = input("Enter Faculty name (or 'done' to finish adding faculty): ")
#         if f_name.lower() == 'done':
#             break
#         branch.faculty.append(f_name)
#     print(f"Course: {branch.name}, Faculty: {branch.faculty}")
