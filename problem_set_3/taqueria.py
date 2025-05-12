item_dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    item_list = get_item_list()
    print()
    print(f"Total:${return_total(item_list)}")


def get_item_list():
    items = []
    while True:
        try:
            item = input("Item: ").strip().title()
            if item not in item_dict:
                print(f"there is no {item}")
                continue
            items.append(item)

        except EOFError:
            break

    return items    

def return_total(item_list):
    total_price = 0
    for item in item_list:
        total_price += item_dict[item]

    return f"{total_price:.2f}"




if __name__ == "__main__":
    main()