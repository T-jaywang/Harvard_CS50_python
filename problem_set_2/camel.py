

camelcase = input("camelCase: ")

sanke_case = ""

for word in camelcase:
    if word.isupper():
        sanke_case += "_" + word.lower()
    else:
        sanke_case += word

print(f"snake_case: {sanke_case}")


