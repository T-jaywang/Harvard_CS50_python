
#the first version 
#with open("students.csv") as file:
    #for line in file:
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        
#the second version 
#with open("students.csv") as file:
	#for line in file:
        #name , house = line.rstrip().split(",")
        #print(f"{name} is in {house}")
        
#the third version
with open("students.csv") as file:
	for line in file:
        name , house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)
        
for student in students:
    print(f"{student['name']} is in {student['house']}")
        
#the forth version
with open("students.csv") as file:
	for line in file:
        name , house = line.rstrip().split(",")
   		student = {"name":name,"house":house}		#the different from version three
        students.append(student)
        
for student in students:
    print(f"{student['name']} is in {student['house']}")
    
#the fifth version
students = []

with open("students.csv") as file:
	for line in file:
        name , house = line.rstrip().split(",")
   		student = {"name":name,"house":house}
        students.append(student)
        
def get_house(student):
    return student["house"]
        
for student in sorted(students, key = get_house):
    print(f"{student['name']} is in {student['house']}")
    
    
    
    
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        