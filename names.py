# first version for write
# name = input("What's your name?")
# file = open("name.txt","w")
# file.write(name)
# file.close()

# second version for write
# name = input("What's your name")
# with open("name.txt","a") as file:
#     file.write(f"{name}\n")

# first version for read
with open("name.txt","r") as file:
    for line in file:
        print("hello,",line.rstrip())