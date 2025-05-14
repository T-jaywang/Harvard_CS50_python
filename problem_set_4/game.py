import random


def main():
    level = get_level()
    ans_number = random_generate_interger(level)
    guess(ans_number)


def get_level():
    while True:
        try:
            n = int(input("Level: ").strip())

            if n < 0 :
                continue

            return n 
        
        except ValueError:
            print("Level must be interger.")


def random_generate_interger(level):
    ans_number = random.randint(1,level + 1)
    return ans_number


def guess(ans_number):
    while True:
        try:
            guess = int(input("Guess: ").strip())

            if guess < 0 :
                continue
            elif guess < ans_number:
                print("Too small!")
                continue
            elif guess > ans_number:
                print("Too large!")
                continue
            else:
                print("Just right!!")
                break

        except ValueError:
            print("Try to guess a integer.")
        

if __name__ == "__main__":
    main()



