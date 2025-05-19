import sys

def main():
    evaluate_arg()
    number = count_line()
    print(number)

def evaluate_arg():
    if len(sys.argv) > 2:
        sys.exit("Too many argument.")
    if len(sys.argv) < 2:
        sys.exit("Too few argument.")
    if not sys.argv[-1].endswith(".py"):
        sys.exit("not python file.")


def count_line():
    number = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line == "":
                    continue
                if line.startswith("#"):
                    continue

                number += 1
            return number

    except FileNotFoundError:
        sys.exit("File not found.")

if __name__ == "__main__":
    main()





