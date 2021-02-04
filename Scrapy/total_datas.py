import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://tr.wikipedia.org/wiki/Ülke_ve_bölgelere_göre_COVID-19_pandemisi")  
soup = BeautifulSoup(htmldata, 'html.parser')  
item = soup.find("table", attrs={"class":"wikitable"}).find("tbody").find_all("tr")

th = item[2].text
th = th.split("\n")
totalConfirmed = th[5]
totalDeaths = th[7]
totalRecovered = th[11]