import requests

while True:
    name = input("Enter a name:") or "()"
    api_url = "https://runbook.expert:10003/greeting?name="+name
    response = requests.get(api_url)
    print(response.json())
