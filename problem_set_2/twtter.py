def main():
    words = input("Input: ")
    output = ""
    for word in words:
        if word in ["A","E","I","O","U"]:
            output += ""
        elif word in ["a","e","i","o","u"]:
            output += ""
        else:
            output += word
    print(f"Output: {output}")


if __name__ == "__main__":
    main()