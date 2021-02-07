import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("la richiesta all'API non è andata a buon fine!")
    data = response.json()
    print("JSON data:", data)


if __name__ == "__main__":
    main()