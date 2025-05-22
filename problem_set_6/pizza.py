import sys
from tabulate import tabulate
import csv

def main():
    evaluate_argus()
    table = read_file()
    print(table)

def evaluate_argus():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")

def read_file():
    try:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("open csv file only.") 

        with open(sys.argv[1],"r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = list(reader)

            return tabulate(rows, headers=headers, tablefmt="grid")
            


    except FileNotFoundError:
        sys.exit("File not found.")


if __name__ == "__main__":
    main()