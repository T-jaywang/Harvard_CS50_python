students = ["Hermione","Herry","Ron"]

def way_one():
    for student in students:
        print(student)

def way_two():
    for i in range(len(students)):
        print(i+1,students[i],sep=":")

way_two()
