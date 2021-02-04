import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://www.worldometers.info/coronavirus/")  
soup = BeautifulSoup(htmldata, 'html.parser')  
item = soup.find("table", attrs={"id":"main_table_countries_today"}).find("tbody").find_all("tr", attrs={"class":"total_row_world"})

newDatas = item[7].text
newDatas = newDatas.split("\n")

newCases = newDatas[4]
newDeaths = newDatas[6]
activeCase = newDatas[9]


#6 new case, 8 new Death