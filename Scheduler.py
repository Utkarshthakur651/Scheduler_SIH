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

# n=int(input("enter number of branches:"))
# for i in range(101,101+n+1):
#     b = input(f"enter branch of {i}:")
#     branches[i]=b
# print(branches)


# x=input("Enter branch_id for faculty registration:")
# e = "y"
# while e == "y":
#     name= input("enter faculty name:")
#     course= input("enter faculty course:")

#     if x in faculty:
#         faculty[x].append([name,])
#     else:
#     faculty[x]=[[name,]]
#     e = input("do you want to continue y/n:")
# # for i in range(101):
# #     f[]
# #     f = input(f"enter faculty of {i}:")
# #     faculty.append(f)


# # cse={1:"",2:"","3":"","4":"","5":"",6:"",7:"",8:""}
# # ece={1:"",2:"","3":"","4":"","5":"",6:"",7:"",8:""}
# # mech={1:"",2:"","3":"","4":"","5":"",6:"",7:"",8:""}
# # civil={1:"",2:"","3":"","4":"","5":"",6:"",7:"",8:""}
# # eee={1:"",2:"","3":"","4":"","5":"",6:"",7:"",8:""}


# # for j in :
# #     i=r.randint(1,8)
# #     if i in phy:
# #         print("phy")
# #     elif i in math:
# #         print("math")
# #     else:
# #         print("none")
