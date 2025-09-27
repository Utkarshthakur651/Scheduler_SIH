from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector as msc
import random,string

app = Flask(__name__)
app.secret_key = "secretkey"

myDB = msc.connect(
    host="localhost", user="root", passwd="@B00y@hmysql", database="schedule"
)
crs = myDB.cursor()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student")
def student():
    return render_template("student_login.html")

@app.route("/admin")
def admin():
    return render_template("admin_login.html")

@app.route("/faculty")
def faculty():
    return render_template("faculty_login.html")

# Handling login submissions (for later authentication logic)
@app.route("/admin_login", methods=["POST"])
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    admin={"1234":"@1234"}

    for a in admin:
        if a==username:
            if admin[a]==password:
                session["user"] = admin[a]
                session["role"] = "admin"
                flash("Admin login successful!", "success")
                return redirect(url_for("admin_dashboard"))   # redirect to dashboard
                break
    else:
        flash("Invalid Admin credentials", "danger")
        return redirect(url_for("admin"))

@app.route("/admin/dashboard")
def admin_dashboard():
    if "user" in session and session.get("role") == "admin":
        return render_template("admin_dashboard.html")
    else:
        flash("You must log in as Admin first", "danger")
        return redirect(url_for("admin"))

@app.route("/logout")
def logout():
    # Clear session data
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))   # Redirect back to home page


@app.route("/admin/add_branch", methods=["GET", "POST"])
def add_branch():
    if "user" not in session or session.get("role") != "admin":
        flash("You must log in as Admin first", "danger")
        return redirect(url_for("admin"))

    if request.method == "POST":
        bid = request.form["bid"]
        bname = request.form["bname"]
        bseats = request.form["bseats"]

        course_names_s1 = request.form.getlist('course_name_s1[]')
        course_ids_s1 = request.form.getlist('course_id_s1[]')
        bcourses_s1 = {
            cid:cname 
            for cname, cid in zip(course_names_s1, course_ids_s1)
        }
        bcourses_s1_str=",".join(["-".join([i,bcourses_s1[i]]) for i in bcourses_s1])

        course_names_s2 = request.form.getlist('course_name_s2[]')
        course_ids_s2 = request.form.getlist('course_id_s2[]')
        bcourses_s2 = {
            cid:cname 
            for cname, cid in zip(course_names_s2, course_ids_s2)
        }
        bcourses_s2_str=",".join(["-".join([i,bcourses_s2[i]]) for i in bcourses_s2])

        try:
            query = """INSERT INTO branch (bid, bname, bseats, bstrength, bcourses_s1, bcourses_s2) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
             
            values = (bid, bname, bseats,0,bcourses_s1_str,bcourses_s2_str)
            crs.execute(query, values)

            crs.execute(f"CREATE TABLE {bname}(sid INT PRIMARY KEY, sname VARCHAR(100), password VARCHAR(100), sbranch VARCHAR(100), semester INT,scourses VARCHAR(255))")
            myDB.commit()

            flash(f"Branch '{bname}' added successfully!", "success")
            return redirect(url_for("add_branch"))

        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("add_branch"))

    return render_template("add_branch.html")

@app.route("/admin/add_student", methods=["GET", "POST"])
def add_student():
    if "user" not in session or session.get("role") != "admin":
        flash("You must log in as Admin first", "danger")
        return redirect(url_for("admin"))

    # Fetch all branches to show in dropdown
    crs.execute("SELECT bname, bid, bseats, bstrength, bcourses_s1, bcourses_s2 FROM branch")
    branches = crs.fetchall()

    if request.method == "POST":
        branch_name = request.form["branch"]
        sname = request.form["sname"]
        semester = int(request.form["semester"])

        # Get branch info
        crs.execute("SELECT * FROM branch WHERE bname = %s", (branch_name,))
        branch = crs.fetchone()
        bid = branch[0]
        bstrength = branch[3]

        # Auto-generate sid
        sid = bid * 1000 + bstrength + 1

        # Auto-generate password (8-char random mix)
        password = "".join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 8))

        # Assign courses based on semester
        courses = branch[4] if semester == 1 else branch[5]

        # Insert into branch table
        query = f"""INSERT INTO {branch_name} (sid, sname, password, sbranch, semester, scourses)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
        crs.execute(query, (sid, sname, password, branch_name, semester, courses))
        myDB.commit()

        # Update branch strength
        crs.execute("UPDATE branch SET bstrength = bstrength + 1 WHERE bid = %s", (bid,))
        myDB.commit()

        flash(f"Student '{sname}' added with ID {sid} and password {password}", "success")
        return redirect(url_for("add_student"))

    return render_template("add_student.html", branches=branches)

@app.route("/admin/add_faculty", methods=["GET", "POST"])
def add_faculty():
    if "user" not in session or session.get("role") != "admin":
        flash("You must log in as Admin first", "danger")
        return redirect(url_for("admin"))

    # Fetch all unique courses to show in dropdown
    crs.execute("SELECT DISTINCT bcourses_s1, bcourses_s2 FROM branch")
    rows = crs.fetchall()
    courses = []
    for row in rows:
        for sem_courses in row:
            if sem_courses:
                for c in sem_courses.split(","):
                    if "-" in c:
                        cid, cname = c.split("-")
                        courses.append((cid.strip(), cname.strip()))
    courses = list(set(courses))  # remove duplicates

    if request.method == "POST":
        fid = request.form["fid"]
        fname = request.form["fname"]
        cid = request.form["course"]

        # Auto-generate password
        password = "".join(random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 8))

        try:
            crs.execute(
                "INSERT INTO faculty (fid, fname, fcourse, password) VALUES (%s, %s, %s, %s)",
                (fid, fname, cid, password),
            )
            myDB.commit()
            flash(f"Faculty '{fname}' added with ID {fid} and password {password}", "success")
            return redirect(url_for("add_faculty"))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for("add_faculty"))

    return render_template("add_faculty.html", courses=courses)

@app.route("/student_login", methods=["POST"])
def student_login():
    sid = request.form["username"]   # Student ID entered
    password = request.form["password"]

    # Check each branch table because students are stored per branch
    crs.execute("SELECT * FROM branch")
    bs = crs.fetchall()

    for branch in bs:
        branch_name = branch[1]
        try:
            query = f"SELECT * FROM {branch_name} WHERE sid = %s AND password = %s"
            crs.execute(query, (sid, password))
            student = crs.fetchone()

            if student:
                session["user"] = student["sname"]
                session["role"] = "student"
                flash("Login successful!", "success")
                return f"Welcome {student[1]}"
        except Exception as e:
            # ignore branches without that student
            continue

    flash("Invalid Student ID or Password", "danger")
    return redirect(url_for("student"))

import random

@app.route("/admin/create_schedule", methods=["GET", "POST"])
def create_schedule():
    if "user" not in session or session.get("role") != "admin":
        flash("You must log in as Admin first", "danger")
        return redirect(url_for("admin"))

    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    schedule = {}
    selected_branch = None

    # Fetch branches for dropdown
    crs.execute("SELECT bname, bid, bstrength, bcourses_s1, bcourses_s2 FROM branch")
    branches = [dict(bname=row[0], bid=row[1], bstrength=row[2],
                     bcourses_s1=row[3], bcourses_s2=row[4]) for row in crs.fetchall()]

    if request.method == "POST":
        selected_branch = request.form["branch"]

        # Get that branch info
        crs.execute("SELECT * FROM branch WHERE bname=%s", (selected_branch,))
        branch = crs.fetchone()
        if branch:
            bid, bname, bseats, bstrength, bcourses_s1, bcourses_s2 = branch
            courses = []
            if bcourses_s1:
                courses.extend([c.split("-")[0] for c in bcourses_s1.split(",")])
            if bcourses_s2:
                courses.extend([c.split("-")[0] for c in bcourses_s2.split(",")])

            # Map course -> faculty
            crs.execute("SELECT fid, fname, fcourse FROM faculty")
            faculties = crs.fetchall()
            faculty_map = {row[2]: row[1] for row in faculties}

            # Rooms
            crs.execute("SELECT room_id FROM classrooms")
            rooms = [r[0] for r in crs.fetchall()]

            # Build schedule {day: [period1..period8]}
            import random
            for day in DAYS:
                daily = []
                for period in range(1, 9):
                    if courses:
                        cid = random.choice(courses)
                        faculty = faculty_map.get(cid, "TBD")
                        room = random.choice(rooms) if rooms else "TBD"
                        daily.append(f"{cid}<br>{faculty}<br>Room {room}")
                    else:
                        daily.append("Free")
                schedule[day] = daily

    return render_template("create_schedule.html",branches=branches, schedule=schedule,selected_branch=selected_branch)



@app.route("/faculty_login", methods=["POST"])
def faculty_login():
    username = request.form["username"]
    password = request.form["password"]
    return f"Faculty {username} logged in with password {password} (demo)."

if __name__ == "__main__":
    app.run(debug=True)

#updateBranchesFromDB()
# while True:
#     exit = mainMenu()
#     if exit:
#         updateDB()
#         myDB.close()
#         print("Exiting...")
#         break
