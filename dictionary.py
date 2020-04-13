student = {
    "name": "John",
    "age": 25,
    "course": ["Math", "compSci"],
    "cell": "616-111-88888",
}
print(student)
print(student["name"])
print(student["course"])
print(student.get("cell"))
print(student.get("phone", "_Not Found_"))
student["phone"] = "555-5555"
print(student.get("phone", "_Not Found_"))
print(student)
student["name"] = "Jane"
print(student)
student.update({"name": "Mary", "age": 33, "phone": "111-1111"})
print(student)
del student["cell"]
print(student)
student.pop("phone")
print(student)
print(len(student))
print(student.values())
print(student.keys())
print(student.items())
for key in student:
    print(key)
for key, value in student.items():
    print(key, value)
