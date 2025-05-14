import random


def main():
    level = get_level()
    problem = generate_problem_dict(level)
    for first_number in problem:
        print(f"{first_number} + {problem[first_number]}")


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())

            if level not in [1,2,3]:
                print("1 <= Level <= 3")
                continue
            
            return level

        except ValueError:
            print("Level must be a interger.")
        

def generate_problem_dict(level):
    problem_dict = {}

    if level == 1:
        for _ in range(10):
            first = random.randint(0,9)
            problem_dict[first]
            problem_dict[first] += random.randint(0,9)

    elif level == 2:
        for _ in range(10):
            first = random.randint(0,99)
            problem_dict[first]
            problem_dict[first] += random.randint(0,99)

    else:
        for _ in range(10):
            first = random.randint(0,999)
            problem_dict[first]
            problem_dict[first] += random.randint(0,999)

    return problem_dict



    

if __name__ == "__main__":
    main()