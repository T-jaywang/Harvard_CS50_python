students = [
    {"name":"Hermione","house":"Gruffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gruffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gruffindor","patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=",")