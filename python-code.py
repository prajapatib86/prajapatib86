
# import requests module
import requests
  
# Making a get request
response = requests.get('https://help.hexagonmi.com/')
  
# print response
print(response)
  
# print request status_code
print(response.status_code)