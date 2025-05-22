def main():
    fraction = input("Fraction: ")
    percentage_fraction = convert(fraction)
    print(gauge(percentage_fraction))


def convert(fraction):
        try:
            x,y = map(int,fraction.split("/"))

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return round((x/y) * 100)
        
        except ValueError:
            raise ValueError("input must be in the form of x/y, where x and y are intergers, and x<= y.")
    
        except ZeroDivisionError:
            raise ZeroDivisionError("y can't be zero.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()