students = []


student1 = {
    "name": "Alice",
    "age": 15,
    "major": "Math",
}

student2 = {
    "name": "Bob",
    "age": 18,
    "major": "Physics",
}

students.append(student1)
students.append(student2)




students[0]["name"] = "Hari"

student2["name"] = "Ramu"


for student in students:
    print(
        f"Name -> {student['name']}  Age -> {student['age']}  Major -> {student['major']}"
    )
