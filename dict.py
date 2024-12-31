student = {
    "name": "Jhon The Don",
    "age": 40,
    "addres": "Banepa",
}


print("Banepa" in student)

student_name = student["name"]
student_age = student.get("age")


student["age"] = 20


print(student)

del student["addres"]

print(student)


for key, value in student.items():
    print(f"key: {key} -> value: {value}")


names = ["ram", "ram"]
names_set = {"ram", "ram", "Hari", "Jhon"}

print("ram" in names_set)


squres = {f"number{x}": x**2 for x in range(10)}

print(squres)
