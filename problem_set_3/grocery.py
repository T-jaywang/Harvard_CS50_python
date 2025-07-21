def main():
    item_list = creat_list()
    output_list(item_list)

def creat_list():
    item_list = {}
    try:
        while True:
            item = input().upper().strip()
            if item not in item_list:
                item_list[item] = 1
            else:
                item_list[item] += 1

    except EOFError:
        return item_list

def output_list(item_list):
    for item in sorted(item_list):
        print(f"{item_list[item]} {item}")

if __name__ == "__main__":
    main()
