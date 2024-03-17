import requests

api=requests.get(url="http://api.open-notify.org/iss-now.json")
#this only stores the response such as 200.Returns the object.

api.raise_for_status() #method to directly show us HTTP error. Without this we get JSON decoder error
#etc.

print (api)
print (api.status_code) #returns only the response code
print(api.json()) #returns the json data of the api

print (api.json()["iss_position"]) #specific json key/value. Same as dictionary.
print (api.json()["iss_position"]["longitude"])