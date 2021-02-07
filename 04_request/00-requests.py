import requests

def main():
    response = requests.get("http://www.google.com")
    print("Status Code: ", response.status_code)
    #print("Headers: ", response.headers)
    #print("Content-Type Header: ", response.headers["Content-Type"])
    print("Contenuto: ", response.text)


if __name__ == "__main__":
    main()