import requests

api=requests.get(url="http://api.open-notify.org/iss-now.json")
#this only stores the response object such as 200.Returns the object.

api.raise_for_status()
#If the status code of the HTTP response is in the range 400-599 (client error or server error),
# raise_for_status() will raise an instance of requests.HTTPError with an appropriate message.
# This allows you to handle error cases in a clean and explicit way.

print (api) #this PRINTS the response object.
print (api.status_code) #returns only the response code
print(api.json()) #returns the json data of the api

print (api.json()["iss_position"]) #specific json key/value. Same as dictionary.
print (api.json()["iss_position"]["longitude"])