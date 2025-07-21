def main():
    plate = input("Plate: ")
    if validate(plate):
        print("Valid")
    else:
        print("Invalid")


def validate(s):
    if not (2 <= len(s) <= 6):
        return False
    
    if s[-1].isalpha():
        return False

    List = []
    for word in s:
        if word.isdigit():
            List.append(word)
    if List[0] == "0":
        return False



    for word in s:
        if word in [",", " ", "-","."]:
            return False

    return True
    
if __name__ == "__main__":
    main()