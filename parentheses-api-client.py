import requests

while True:
    string = input("Enter a string:") or "()"
    api_url = "https://runbook.adob71.com:10002/parentheses/"+string
    response = requests.get(api_url)
    print(response.json())
