#the first version
#import re

#url = input("URL: ").strip()

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "" , url)
#print(f"Username : {username}")

#the second version
# import re

# url = input("Url: ").strip()

# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)" , url, re.IGNORECASE):
#     print(f"Username: " , matches.group(1))