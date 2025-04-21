
def main():
    name = input ("What is your name? ").strip().title()
    hello(name)

def hello(to = "world"): #default output "Hello, world"
    print(f"Hello, {to}")

main()

def hello_to_friend():
    print("hellow \"friend\"") #backslash actually represents an escape character




