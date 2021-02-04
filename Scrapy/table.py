import requests  
from bs4 import BeautifulSoup  
import json
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory")  
soup = BeautifulSoup(htmldata, 'html.parser')  
item = soup.find("table", attrs={"class":"wikitable"}).find_all("tbody")
item = item[0].find_all("tr")

countries = []
totalCases = []
totalDeaths = []
totalRecovered = []
for i in range(2,12):
    country = item[i].text
    country = country.split("\n")
    countries.append(country[3])
    totalCases.append(country[5])
    totalDeaths.append(country[7])
    totalRecovered.append(country[9])

