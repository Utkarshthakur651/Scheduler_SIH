import random as r

branches = {}
courses_fac = {}

z = "y"
while z == "y":
    course = input("enter course name:")
    w = "y"
    n = 0
    while w == "y":
        if course not in courses_fac:
            courses_fac[course] = []
            courses_fac[course].append(len(courses_fac[course]))

        f_name = input("enter faculty name:")
        courses_fac[course].append(f_name)
        w = input("do you want to add more faculty for this course y/n:")

    z = input("do you want to continue y/n:")
print(courses_fac)
