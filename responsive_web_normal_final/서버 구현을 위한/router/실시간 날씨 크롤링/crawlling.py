from bs4 import BeautifulSoup
import requests

Userlocation = '33.49,126.45' #csv 장소

url = 'https://weather.com/weather/today/l/' + Userlocation 

html = requests.get(url)
bs_html = BeautifulSoup(html.content, "html.parser")

Todaystate = bs_html.find('div', {"data-testid":"wxPhrase"})
NowTem = Todaystate.find('span', {"class":"CurrentConditions--tempValue--3a50n"})

print(Todaystate)
print(NowTem)
