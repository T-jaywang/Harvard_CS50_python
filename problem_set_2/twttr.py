def main():
    words = get_words()
    print(replace_alphabat(words))

def get_words():
    words = input("Input: ")
    return words

def replace_alphabat(words):
    output = ""
    for word in words:
        if word in ["A","E","I","O","U"]:
            output += ""
        elif word in ["a","e","i","o","u"]:
            output += ""
        else:
            output += word
    return f"Output: {output}"


if __name__ == "__main__":
    main()