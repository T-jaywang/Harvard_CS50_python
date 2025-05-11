expression = input("Expression: ")

x,y,z = expression.split(" ")

if y == "+":
    ans = float(x) + float(z)
elif y == "-":
    ans = float(x) - float(z)
elif y == "*":
    ans = float(x) * float(z)
elif y == "/":
    ans = float(x) / float(z)

print(ans)








