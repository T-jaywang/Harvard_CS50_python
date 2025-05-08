# THE FIRST VERSION
# students = [
#     {"name" : "Hermione", "house" : "Gryffindor"},
#     {"name" : "Harry", "house" : "Gryffindor"},
#     {"name" : "Ron", "house" : "Gryffindor"},
#     {"name" : "Draco", "house" : "Slytherin"},
#     {"name" : "Padma", "house" : "Ravenclaw"},
# ]

# gryffindor = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindor):
#     print(gryffindor)

# THE SECOND VERSION
# students = [
#     {"name" : "Hermione", "house" : "Gryffindor"},
#     {"name" : "Harry", "house" : "Gryffindor"},
#     {"name" : "Ron", "house" : "Gryffindor"},
#     {"name" : "Draco", "house" : "Slytherin"},
#     {"name" : "Padma", "house" : "Ravenclaw"},
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

# THE THIRD VERSION
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)

# THE FOURTH VERSION
# students = ["Hermione", "Harry", "Ron"]
# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

# THE FIFTH VERSION
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# THE SIXTH VERSION
# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students):
#     print(i + 1, students[i])

# THE SEVENTH VERSION
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])