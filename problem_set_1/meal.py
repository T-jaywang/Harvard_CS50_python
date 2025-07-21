def main():
    time = get_time()

    if time.endswith("a.m."):
        time = process_time_am(time)
    else:
        time = process_time_pm(time)

    hours = calculate_how_many_hours(time)

    if 7 <= hours < 8:
        print("breakfast time")
    elif 12 <= hours < 13:
        print("lunch time")
    elif 18 <= hours < 19:
        print("dinner time")

def get_time():
    time = input("What time is it?").strip()
    return time

def process_time_am(time):
    time = time.replace("a.m.","")
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if hour == 12:
        hour = 0
    time = f"{hour}:{minute}"
    
    return time

def process_time_pm(time):
    time = time.replace("p.m.","")
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if hour == 12:
        pass
    else:
        hour += 12
    time = f"{hour}:{minute}"

    return time

def calculate_how_many_hours(time):
    hour , minute = time.split(":")
    minute = float(minute) / 60
    hour = float(hour)

    return hour + float(minute)


if __name__ == "__main__":
    main()