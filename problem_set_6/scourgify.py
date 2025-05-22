import sys
import csv


def main():
    evaluate_args()
    data = read_file()
    write_file(data)



def evaluate_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")


def read_file():
    data = []       
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                full_name = row["name"].replace('"','')
                last, first = full_name.split(", ")
                
                student = {
                    "first":first,
                    "last":last,
                    "house":row["house"]
                }
                data.append(student)

        return data
    
    except FileNotFoundError:
        sys.exit("File not found.")


def write_file(data):
    try:
        with open(sys.argv[2],"w",newline="") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()

            for row in data:
                writer.writerow(row)
    
    except FileNotFoundError:
        sys.exit("File not found.")

if __name__ == "__main__":
    main()