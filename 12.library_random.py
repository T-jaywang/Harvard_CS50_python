import random
import statistics

def flip_coin():
    coin = random.choice(["heads","tails"])
    print(coin)

def random_number():
    number = random.randint(1,10)
    print(number)

def shuffle_cards():
    cards = ["jack","queen","king"]
    random.shuffle(cards)
    for card in cards:
        print(card)

def average_score():
    print(statistics.mean([100,90]))

