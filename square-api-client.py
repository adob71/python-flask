import requests

while True:
    x = input("Enter a number:") or "1"
#    api_url = "http://localhost:10001/square/"+x
    api_url = "https://runbook.expert:10001/square/"+x
    response = requests.get(api_url)
    print(response.json())
