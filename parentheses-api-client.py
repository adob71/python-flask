import requests

while True:
    string = input("Enter a string:") or "()"
    api_url = "https://runbook.expert:10002/parentheses/"+string
    response = requests.get(api_url)
    print(response.json())
