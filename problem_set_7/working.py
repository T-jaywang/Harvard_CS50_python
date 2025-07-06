import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time.")
    
    h1, m1, ap1, h2, m2, ap2 = match.groups()

    if m1 is None:
        m1 = 0
    else:
        m1 = int(m1)
    if m2 is None:
        m2 = 0
    else:
        m2 = int(m2)
        
    h1 = int(h1)
    h2 = int(h2)

    if not 0 <= m1 < 60 or not 0 <= m2 < 60:
        raise ValueError("Invalid time.")

    h1 = turn_12_to_24(h1, ap1)
    h2 = turn_12_to_24(h2, ap2)

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    


def turn_12_to_24(hour, ampm):
    if ampm == "AM":
        return 0 if hour == 12 else hour
    if ampm == "PM":
        return 12 if hour == 12 else hour + 12
    


if __name__ == "__main__":
    main()