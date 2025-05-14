import inflect
p = inflect.engine()

def main():
    name_list = get_input()
    bid_adieu_output(name_list)


def get_input():    #prompts the user for their name, one per line, until user press control-d, and input at least one name.
    name_list = []
    
    while True:
        try:
            name = input("Name: ").strip()
            name_list.append(name)

        except EOFError:
            if len(name_list) == 0:
                print("You must input at least one name.")
            
            return name_list
        


def bid_adieu_output(name_list):

    print("Adieu, adieu, to ",p.join(name_list))



if __name__ == "__main__":
    main()