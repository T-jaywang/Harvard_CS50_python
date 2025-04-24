#the first version
#email = input("What's your email?").strip

#username, domain = email.split("@")

#if username and domain.endswith(".edu"):
    #print("Vaild")
#else:
    #print("Invalid")


#the second version
#import re 

#email = input("What's your email?").strip

#if re.search(r"^[^@]+@[^@]+\.edu$" , email):
    #print("Vaild")
#else:
    #print("Invalid")

#the third version
# import re

# email = input("What's your email").strip()

# if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email , re.IGNORECASE):   #[a-zA-Z0-9_] = \w
#     print("Valid")
# else:
#     print("Invalid")
