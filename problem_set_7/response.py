from validator_collection import validators, errors, checkers
import sys

def main():
    get_email()
    print("Valid")

def get_email():
    try:
        email_address = validators.email(input("What's your email address?"))

    except errors.EmptyValueError:
        sys.exit("Empty input.")
    except errors.InvalidEmailError:
        sys.exit("Invalid email.")


if __name__ == "__main__":
    main()