import requests
import sys
import json

def main():
    (data,number) = request()
    ans = data_output(data,number)
    print(ans)

    

def request():
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument.")
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")
        


    url = f"https://rest.coincap.io/v3/assets/bitcoin"

    headers = {
        "Authorization": "Bearer 674c492a7889af5d651a5913f2a8668685f6d289e23a98172c139df7f6bbdd35"
    }

    try:
        response = requests.get(url, headers=headers)
    except requests.RequestException:
        sys.exit("Request error.")

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))
        return (data,number)
    else:
        sys.exit("request error!")


def data_output(data,number):
    price = float(data["data"]["priceUsd"])
    ans = f"${number * price}"

    return ans



if __name__ == "__main__":
    main()



