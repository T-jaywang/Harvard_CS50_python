from datetime import date
import inflect
import sys
import re


def main():
    birth = input("Date of Birth: ")
    birth_date = validate_date(birth)
    minute = convert_date_to_minute(birth_date)
    minute_str = convert_minute_to_str(minute)
    print(minute_str)

def validate_date(birth):
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    if not re.search(pattern, birth):
        sys.exit("Invalid date.")
    
    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date.")

    return birth_date

def convert_date_to_minute(birth_date):
    today_date = date.today()
    delta = today_date - birth_date
    minute = delta.days * 24 * 60
    return minute

def convert_minute_to_str(minute):
    p = inflect.engine()
    number = p.number_to_words(minute)
    return number

if __name__ == "__main__":
    main()