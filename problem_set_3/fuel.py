def main():
    x,y = get_input()
    number = division_to_precent(x,y)
    print(percent(number))
    


def get_input():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            x,y = map(int,fraction.split("/"))

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            
            return x,y

        except ValueError:
            print("input must be in the form of x/y, where x and y are intergers, and x<= y.")
        except ZeroDivisionError:
            print("y can't be zero.")
        



def division_to_precent(x,y):
    return round((x / y) * 100)

def percent(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"{p}%"
    


    
if __name__ == "__main__":
    main()