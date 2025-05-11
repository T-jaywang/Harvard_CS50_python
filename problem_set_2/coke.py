
def main():
    price = 50
    while price != 0:
        print(f"Amount Due: {price}")
        coin = get_coin()
        price -= coin
        if price < 0:
            break
    print(f"Change Owed: {abs(price)}")


def get_coin():
    coin = int(input("Insert coin: "))
    if coin not in [5,10,25]:
        coin = 0
    return coin



if __name__ == "__main__":
    main()