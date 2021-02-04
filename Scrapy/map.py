import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory")  
soup = BeautifulSoup(htmldata, 'html.parser')  
item = soup.find_all('img', attrs={"class":"thumbimage"})
print(item[0]["src"])