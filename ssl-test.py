import requests
 
# creating Session object and
# declaring the verify variable to False
session = requests.Session()
session.verify = False
 
# sending a get http request to specified url
response = requests.get("https://help.hexagonmi.com/")
 
# response data
print(response.text)