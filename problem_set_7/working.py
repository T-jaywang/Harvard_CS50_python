import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern,s)
    
    h1, m1, ap1, h2, m2, ap2 = match.groups()

    h1 = int(h1)
    h2 = int(h2)

    if not match:
        raise ValueError("Invalid time.")
    if m1:
        m1 = int(m1)
        0 <= m1 <60
    else:
        raise ValueError("Invalid time.")
    if m2:
        m2 = int(m2)
        0 <= m2 < 60 
    else:
        raise ValueError("Invalid time.")

    h1 = to_24_hour(h1, ap1)
    h2 = to_24_hour(h2, ap2)

    if m1 is None:
        m1 = 0
    if m2 is None:
        m2 = 0

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def to_24_hour(hour, ampm):
    if ampm == "AM":
        return 0 if hour == 12 else hour
    if ampm == "PM":
        return 12 if hour == 12 else hour + 12

    

    
if __name__ == "__main__":
    main()