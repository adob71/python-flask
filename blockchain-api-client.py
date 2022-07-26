import requests

while True:
    string = input("Enter: mine_block, get_chain, valid\n") or "mine_block"
    api_url = "https://bitcoinexplorer.adob71.com:10001/"+string
    response = requests.get(api_url)
    print(response.json())
    print ()
