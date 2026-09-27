#Samuel Guizar
#9/26/26
#Module 9.2 Assignment

#This program tests connection, gets data, then formats the JSON response

#Import necessary libraries
import requests
import json

#Test connection and get data
response = requests.get('https://digimon-api.vercel.app/api/digimon')
print("API connection status:", response.status_code)

#Print response with no formatting
print("\nResponse with no formatting:")
print(response.text)

#Format the JSON response
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Print formatted response
print("\nFormatted response:")
jprint(response.json())