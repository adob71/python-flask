import requests

while True:
    x = input("Enter a number:") or "1"
    api_url = "https://runbook.expert:10001/square/"+x
    response = requests.get(api_url)
    print(response.json())
