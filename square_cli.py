import requests

while True:
    x = input("Enter x:") or "1"
    api_url = "http://localhost:10001/square/"+x
    response = requests.get(api_url)
    print(response.json())
