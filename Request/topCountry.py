import requests
import json

url = "https://api.covid19api.com/summary"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
result = json.loads(response.text)
totalConf= []

for i in range(len(result["Countries"])):
    totalConf.append(result["Countries"][i])
ordered_list = sorted(result["Countries"], key= lambda d : (d["TotalConfirmed"]),reverse= True)

