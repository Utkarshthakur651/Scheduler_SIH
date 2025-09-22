import mysql.connector as msc
import random

myDB = msc.connect(
    host="localhost", user="root", passwd="@B00y@hmysql", database="schedule"
)
crs = myDB.cursor()


branches = {} #{bid:branch_object}

unique_bcourses = {cid:branches[bid].bcourses[sem][cid] 
            for bid in branches
            for sem in branches[bid].bcourses
            for cid in sem
            if cid not in unique_bcourses
        }
pending = {i: 0 for i in unique_bcourses}

class Branch:
    def __init__(self, bid):
        self.bid = bid
        self.bname =""
        self.bseats = 0
        self.bcourses = []  # [{cid1:course1, cid2:course2},{cid1:course1,cid2:course2}]
        self.bstudents = {}  # {sid:[sid, sname, password, sbranch, sem, scourses]}
        self.bstrength = len(self.bstudents)

        self.bschedule = []

    def addBranch(self):
        self.bname = input("Enter Branch name:")
        self.bseats = int(input("Enter Branch seats:"))
        for sem in [1, 2]:
            print(f"Enter courses offered in semester {sem}:")
            self.bcourses.append({})
            c = 1
            while True:
                try:
                    course = input(f"Enter course{c} (or 'done' to finish): ").strip()
                    if course.lower() == "done":
                        break
                    if course in self.bcourses:
                        print(
                            f"Course {course} already added. Please enter a different course."
                        )
                    else:
                        cid = input(f"Enter course ID for {course}: ").strip()
                        self.bcourses[sem - 1][cid] = course
                        c+= 1
                except Exception as e:
                    print(f"Error: {e}. Please enter the course again.")

        print(f"Branch {self.bname} added with BID:{self.bid}.")

    def addStudent(self):
        sid = self.bid * 1000 + self.bstrength + 1
        print(f"Student ID: {sid}")

        sname = input("Enter Student name: ")

        password = ""
        for i in random.sample(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 8
        ):
            for j in i:
                password += j

        sem = int(input("Enter semester for in which student is right now: "))
        scourses = self.bcourses[0] if sem == 1 else self.bcourses[1]

        self.bstudents[sid] = [sid, sname, password, self.bname, sem, scourses]
        
        print(f"Student {sname} added to database with password:{password}.\n")


    def is_slot_free(day, period, fid, room_id, bid):
        crs.execute(f"select * from schedule where day='{day}' and period={period}")
        slot = crs.fetchall()
        print(slot)
        print(type(slot))
        # if slot == None:
        # for fid
        # return True

    
    def showBranch(self):
        print(f"""
        {self.bid}
        {self.bname}
        {self.bstudents}
        {self.bseats}
        {self.bstrength}
        {self.bcourses }
        """
        )

def updateDB():
    crs.execute("select * from branch")
    d=crs.fetchall()
    for bid in branches:
        for row in d:
            if row[0]==bid:
                crs.execute(f'''UPDATE branch (
                    bid=%s,
                    bname=%s, 
                    bseats=%s, 
                    bstrength=s%, 
                    bcourses_s1=%s, 
                    bcourses_s2=%s
                    WHERE bid={bid}''',)
                
                crs.execute(f"select * from {branches[bid].bname}")
                Students=crs.fetcall()
                for i in branches[bid].students:
                    s=branches[bid].students
                    for row in Students:
                        if row[0]==i:
                            crs.execute(f'''UPDATE {branches[bid].bname}(
                                sid=%s,
                                sname=%s,
                                password=%s, 
                                sbranch=%s, 
                                semester=%s, 
                                scourses=%s
                                WHERE sid={i}
                                ''',(s[i][0],s[i][1],s[i][2],s[i][3],s[i][4],s[i][5]))
                    else:
                        crs.execute(f'''INSERT INTO {branches[bid].bname}(
                            sid=%s,
                            sname=%s,
                            password=%s, 
                            sbranch=%s, 
                            semester=%s, 
                            scourses=%s
                            ''',(s[i][0],s[i][1],s[i][2],s[i][3],s[i][4],s[i][5]))
                    
        else:
            query1 = f'''INSERT INTO branch (bid, bname, bseats, bstrength, bcourses_s1, bcourses_s2) 
            VALUES (%s, %s, %s, %s, %s, %s)'''
            values1 = (
            bid,
            branches[bid].bname,
            branches[bid].bseats,
            branches[bid].bstrength,
            ",".join(["-".join([i,branches[bid].bcourses[0][i]]) for i in branches[bid].bcourses[0]]),
            ",".join(["-".join([i,branches[bid].bcourses[1][i]]) for i in branches[bid].bcourses[1]]))
            crs.execute(query1, values1)

            crs.execute(f"CREATE TABLE {branches[bid].bname}(sid INT PRIMARY KEY, sname VARCHAR(100), password VARCHAR(100), sbranch VARCHAR(100), semester INT,scourses VARCHAR(255))")

            s=branches[bid].bstudents
            for i in s:
                query2=f"INSERT INTO {branches[bid].bname}(sid,sname,password,sbranch,semester,scourses) VALUES(%s,%s,%s,%s,%s,%s)"
                values2 = (s[i][0], s[i][1], s[i][2], s[i][3], s[i][4], ",".join(["-".join([j,s[i][5][j]]) for j in s[i][5]]))
                crs.execute(query2, values2)

        myDB.commit()


def mainMenu():
    print("\n\t\tMain Menu\n")
    print("1. Add Branch")
    print("2. Add Student")
    print("3. Add Faculty")
    print("4. Add Classroom")
    print("5. Create Schedule")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice not in [1, 2, 3, 4, 5, 6]:
        print("Invalid choice")
        mainMenu()

    elif choice == 6:
        return True

    elif choice == 1:
        print("\n\t\tBranch Addition Menu")
        while True:
            bid = int(input("\nEnter Branch ID: "))
            if bid not in branches:
                branches[bid] = Branch(bid)
                branches[bid].addBranch()
            else:
                print(f"Branch with Branch ID:{bid}, Branch name:{branches[bid].bname} already exists.")

            exit = input("Do you want to add more Branches? (y/n): ")
            if exit.lower() == "n":
                break

    elif choice == 2:
        print("\n\t\tStudent Addition Menu\n")
        while True:
            print("Available Branches:")
            ava_br={}
            for c, i in zip(branches, range(1, len(branches) + 1)):
                print(f"{i}.{branches[c].bname}")
                ava_br[i]=c


            bno = int(input("\nEnter Branch no. from above:"))
            if bno in ava_br:
                branches[ava_br[bno]].addStudent()
            else:
                print(
                    f"Branch does not exist. Please add the branch first."
                )

            exit = input("Do you want to add more students? (y/n): ")
            if exit.lower() == "n":
                break


while True:
    exit = mainMenu()
    if exit:
        updateDB()
        myDB.close()
        print("Exiting...")
        break
