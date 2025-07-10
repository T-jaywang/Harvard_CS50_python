
def main():
    dollers = get_dollers()
    percent = get_percentage()
    tip = dollers * (percent/100)
    print(f"Leave ${tip:.2f}")

def get_dollers():
    dollers = input("How much was the meal: ")
    return float(dollers)

def get_percentage():
    percent = input("Precentage you like to tip: ")
    return float(percent)


if __name__ == "__main__":
    main()