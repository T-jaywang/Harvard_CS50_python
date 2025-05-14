months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date_list = get_date_list()
    print(transfer_ISO_type(date_list))


def get_date_list():
    while True:
        date = input().strip()

        if "," in date:     # MONTH day, year type
            date_list = date.split(" ")

            if len(date_list) != 3:
                continue

            month_str = date_list[0]
            day = date_list[1].replace(",","")
            year = date_list[2]

            if month_str not in months_list:
                continue
            
            day = int(day)

            if not 1 <= day <= 31:
                continue
            
            return [month_str, day, year]
            

        else:               # MM-DD-YYYY type
             date_list = date.split("/")

             if len(date_list) != 3:
                 continue
             
             month = date_list[0]
             day = date_list[1]
             year = date_list[2]

             month, day, year = map(int,(month,day,year))

             if not 1 <= day <= 31:
                 continue
             if not 1 <= month <= 12:
                 continue

             return [month,day,year]
    

def transfer_ISO_type(date_list):

    if date_list[0] in months_list:

        month, day, year  = date_list
        month = months_list.index(month) + 1
        month, day, year = map(int,(month,day,year))

        return f"{year:04}-{month:02}-{day:02}"


    else:
        month, day, year = map(int,date_list)

        return f"{year:04}-{month:02}-{day:02}"




if __name__ == "__main__":
    main()