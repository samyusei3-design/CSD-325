#Samuel Guizar
#9/25/26
#Module 9.2 Assignment

#This program tests connection, gets data, then formats the JSON response

#Import necessary libraries
import requests
import json

#Test and get astronaut data
response = requests.get('http://api.open-notify.org/astros.json')
print("Astronaut API status:", response.status_code)

#Print astronaut response
print("Astronaut response:")
print(response.json())

#Format the JSON response
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Print formatted astronaut response
print("\nFormatted astronaut response:")
jprint(response.json())