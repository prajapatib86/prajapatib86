import requests

response = requests.get("https://help.hexagonmi.com/", verify=False)

if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed with status code:", response.status_code)