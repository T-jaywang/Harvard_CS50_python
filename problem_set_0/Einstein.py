
def main():
    kilogram = get_kilogram()
    energy = kilogram_convert_energy(kilogram)
    print(energy)

def get_kilogram():
    m = float(input("How many kg?"))
    return m

def kilogram_convert_energy(m):
    c = 3 * 10 ** 8
    E = m * (c ** 2)
    return E

if __name__ == "__main__":
    main()