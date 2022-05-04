import requests

while True:
    str = input("Enter str:") or "()"
    api_url = "http://localhost:10002/parentheses/"+str
    response = requests.get(api_url)
    print(response.json())


# Driver code
#string = "{[]{()}}"
#print(string,"-", check(string))
#
#string = "[{}{})(]"
#print(string,"-", check(string))
#
#string = "((()"
#print(string,"-",check(string))
