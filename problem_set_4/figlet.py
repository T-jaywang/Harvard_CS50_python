import sys
from pyfiglet import Figlet
import random


def main():
    if len(sys.argv) == 1:  #output text in a random font

        figlet = Figlet()
        fonts = figlet.getFonts()
        figlet.setFont(font=random.choice(fonts))

        word = get_input()
        print(figlet.renderText(word))


    elif len(sys.argv) == 3:  #output text in a specific font
        
        if sys.argv[1] not in ["-f","--font"]:
            sys.exit("Invalid option. use -f or --font.")

        figlet = Figlet()
        fonts = figlet.getFonts()

        if sys.argv[2] not in fonts:
            sys.exit("Font not found.")

        figlet.setFont(font=sys.argv[2])

        word = get_input()
        print(figlet.renderText(word))

    else:
        print("terminal input syntax: [-f or --font ,FONT]")

def get_input():
    while True:
        try:
            word = input("Input: ").strip()
            if not word:
                raise ValueError("Input cannot be empty.")
            
            return word
        
        except ValueError as e:
            print(e)
    

if __name__ == "__main__":
    main()