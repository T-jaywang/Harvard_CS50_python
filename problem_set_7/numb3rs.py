import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^\d+\.\d+\.\d+\.\d+$"

    if not re.search(pattern, ip):
        return False
    
    number_list = ip.split(".")
    for number in number_list:
        number = int(number)
        if not 0 <= number <= 255:
            return False
        
    return True
        




    


if __name__ == "__main__":
    main()