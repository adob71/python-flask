import requests

while True:
    str = input("Enter str:") or "()"
#    api_url = "http://localhost:10002/parentheses/"+str
    api_url = "https://runbook.expert:10002/parentheses/"+str
    response = requests.get(api_url)
    print(response.json())
