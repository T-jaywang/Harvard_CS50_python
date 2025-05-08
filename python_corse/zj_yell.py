# THE FIRST VERSION
# def main():
#     yell(["This", "Is", "CS50"])


# def yell(words):
#     uppercase = []
#     for word in words:
#         uppercase.append(word.upper())
    
#     print(*uppercase)

# if __name__ == "__main__":
#     main()

# THE SECOND VERSION
# def main():
#     yell("This", "Is", "CS50")


# def yell(*words):
#     uppercase = []
#     for word in words:
#         uppercase.append(word.upper())
    
#     print(*uppercase)

# if __name__ == "__main__":
#     main()

# THE THIRD VERSION
# def main():
#     yell("This", "Is", "CS50")


# def yell(*words):
#     uppercase = map(str.upper, words)
#     print(*uppercase)

# if __name__ == "__main__":
#     main()

# THE FOURTH VERSION
def main():
    yell("This", "Is", "CS50")


def yell(*words):
    uppercase = [word.upper() for word in words]
    print(*uppercase)

if __name__ == "__main__":
    main()