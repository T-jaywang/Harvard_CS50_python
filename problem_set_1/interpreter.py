def main():
    x, y, z = get_expression()
    answer = caculate(x, y, z)
    print(answer)

def get_expression():
    expression = input("Expression: ")
    x,y,z = expression.split(" ")
    return(x, y, z)

def caculate(x, y, z):
    if y == "+":
        ans = float(x) + float(z)
    elif y == "-":
        ans = float(x) - float(z)
    elif y == "*":
        ans = float(x) * float(z)
    elif y == "/":
        ans = float(x) / float(z)

    return ans

if __name__ == "__main__":
    main()








