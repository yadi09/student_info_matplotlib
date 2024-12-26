from flask import Flask, render_template, request, redirect, url_for # type: ignore
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Data storage
students_data = [
    {"name": "Yadamzer", "gender": "Male", "gpa": 3.0},
    {"name": "Afework", "gender": "Male", "gpa": 3.5},
    {"name": "Tekalgn", "gender": "Male", "gpa": 3.9},
    {"name": "Serkalem", "gender": "Female", "gpa": 4.0},
    {"name": "Beletu", "gender": "Female", "gpa": 2.1},
    {"name": "Regasa", "gender": "Male", "gpa": 0.5},
    {"name": "Demekech", "gender": "Female", "gpa": 2.7},
    {"name": "Alemitu", "gender": "Female", "gpa": 1.4},
    {"name": "zelalem", "gender": "Male", "gpa": 3.4},
    {"name": "abel", "gender": "Male", "gpa": 2.9},
]

# function to generate diagrams
def generate_diagrams():
    # GPA to generate diagrams
    names = [student["name"] for student in students_data]
    gpas = [student["gpa"] for student in students_data]
    plt.bar(names, gpas, color='blue', alpha=0.7)
    plt.title("GPA Distribution")
    plt.xlabel("Students")
    plt.ylabel("GPA")
    plt.ylim(0, 4.0)
    plt.savefig("static/diagrams/gpa_chart.png")
    plt.close()

    # Gender count to generate diagrams
    gender_count = {"Male": 0, "Female": 0}
    for student in students_data:
        gender_count[student["gender"]] += 1
    genders = list(gender_count.keys())
    totals = list(gender_count.values())
    print("The", genders[0], "total is:", totals[0], "And The", genders[1], "total is:", totals[1])
    colors = ['green', 'yellow']
    plt.pie(totals, labels=genders, colors=colors, autopct='%1.1f%%')
    plt.title("Gender Distribution")
    plt.savefig("static/diagrams/gender_chart.png")
    plt.close()

# index route
@app.route('/')
def index():
    generate_diagrams()
    return render_template("index.html", students=students_data)

# Add student route
@app.route('/add', methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]
        gpa = float(request.form["gpa"])
        students_data.append({"name": name, "gender": gender, "gpa": gpa})
        return redirect(url_for("index"))
    return render_template("add_student.html")

if __name__ == '__main__':
    if not os.path.exists("static/diagrams"):
        os.makedirs("static/diagrams")
    app.run(debug=True)
