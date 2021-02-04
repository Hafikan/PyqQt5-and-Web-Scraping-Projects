import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://www.worldometers.info/coronavirus/")  
soup = BeautifulSoup(htmldata, 'html.parser')  
item = soup.find("table", attrs={"id":"main_table_countries_today"}).find("tbody").find_all("tr")


countries = []

for i in range(8,226):
    item[i] = item[i].text
    item[i] = item[i].split("\n")
    countries.append(item[i])
    

#3 total Case
#4 new case
#5 total deaths
#6 new deaths
#7 total recovered
#9 active case
#13 total test