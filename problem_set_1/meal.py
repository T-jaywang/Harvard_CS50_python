def main():
    time = input("What time is it?")
    
    if time.endswith("a.m."):
        time = time.replace("a.m.","")
    elif time.endswith("p.m."):
        time = time.replace("p.m.","")
        hour , minute = time.split(":")
        hour = int(hour)
        minute = int(minute)
        if hour != 12:
            hour += 12
        
        time = f"{hour}:{minute}"

    num = convert(time)

    if 7 <= num < 8:
        print("breakfast time")
    elif 12 <= num < 13:
        print("lunch time")
    elif 18 <= num < 19:
        print("dinner time")
    

def convert(time):
    hour , minute = time.split(":")
    minute = float(minute) / 60
    hour = float(hour)

    return hour + float(minute)


if __name__ == "__main__":
    main()