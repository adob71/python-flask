import requests

while True:
    string = input("Enter mine_block, get_chain, valid:") or "mine_block"
    api_url = "https://runbook.adob71.com:10001/"+string
    response = requests.get(api_url)
    print(response.json())
