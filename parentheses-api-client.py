import requests

while True:
    str = input("Enter a string:") or "()"
    api_url = "https://runbook.expert:10002/parentheses/"+str
    response = requests.get(api_url)
    print(response.json())
