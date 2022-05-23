import requests

while True:
    str = input("Enter a name:") or "()"
    api_url = "https://runbook.expert:10003/greeting?name="+str
    response = requests.get(api_url)
    print(response.json())
