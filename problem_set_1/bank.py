def main():
    greet = get_greet()
    n = evaluate_greet(greet)
    print(n)
    
def evaluate_greet(greet):
    if greet.startswith("hello"):
        return("$0")
    elif greet.startswith("h"):
        return("$20")
    else:
        return("$100")

def get_greet():
    greet = input("Greeting:").strip().lower()
    return greet

if __name__ == "__main__":
    main()
    