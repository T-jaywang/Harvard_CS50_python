
# the first version 
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
        
#the second version 
# with open("students.csv") as file:
# 	for line in file:
# 		name , house = line.rstrip().split(",")
# 		print(f"{name} is in {house}")
        
# the third version
# students = []

# with open("students.csv") as file:
# 	for line in file:
# 		name , house = line.rstrip().split(",")
# 		student = {}
# 		student["name"] = name
# 		student["house"] = house
# 		students.append(student)
        
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
        
# #the forth version
# students = []

# with open("students.csv") as file:
# 	for line in file:
# 		name , house = line.rstrip().split(",")
# 		student = {"name":name,"house":house}		#the different from version three
# 		students.append(student)
        
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
    
# #the fifth version
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         student = {"name":name,"house":house}
#         students.append(student)
        
# def get_house(student):
#     return student["house"]

# for student in sorted(students, key = get_house):
#     print(f"{student['name']} is in {student['house']}")
    
# the sixth version
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         student = {"name":name,"house":house}
#         students.append(student)

# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is in {student['house']}")
    
# the seventh version
# import csv

# students = []

# with open("students_home.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name":name,"home":home})

# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is in {student['home']}")
    
# the ninth version
# import csv

# students = []

# with open("students_home.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name":row["name"],"home":row["home"]})

# for student in sorted(students, key = lambda student : student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# the tenth version
# import csv

# name = input("What's your name?")
# home = input("What's your home?")

# with open("students.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([[name,home]])
        
# the eleventh version
# import csv

# name = input("What's your name?")
# home = input("What's your home?")

# with open("students.csv","a") as file:
#     writer = csv.DictWriter(file,fieldnames=["name","home"])
#     writer.writerow({"name":name,"home":home})
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        