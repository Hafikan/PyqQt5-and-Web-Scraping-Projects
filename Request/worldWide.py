import requests 
import json

url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

result = json.loads(response.text)


totalConfirmed = result["Global"]["TotalConfirmed"]
totalRecovered = result["Global"]["TotalRecovered"]
totalDeaths = result["Global"]["TotalDeaths"]
newConfirmed = result["Global"]["NewConfirmed"]
newDeaths = result["Global"]["NewDeaths"]
newRecovered = result["Global"]["NewRecovered"]
