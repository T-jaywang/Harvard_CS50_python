def main():
    for _ in range(get_number()):
        print("meow")

    
def get_number():
    while True:
        number = int(input("How many times you want to meow?"))
        if number > 0:
            return number
        
main()

