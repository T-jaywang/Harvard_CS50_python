def main():
    ans = get_answer()
    print(evaluate_answer(ans))


def get_answer():
    ans = input("What is the Answer to the Great Queen of Life, the Universe, and Everything?").strip().lower()
    return ans

def evaluate_answer(ans):
    correct_ans = [42, "42", "forty-two", "forty two"]
    if ans in correct_ans:
        return("Answer correct!")
    else:
        return("Wrong answer!")
    
if __name__ == "__main__":
    main()






