from bs4 import BeautifulSoup
import requests
import pandas as pd

WorldNations=[]

url = ('https://www.scrapethissite.com/pages/simple/')
html_text = requests.get(url)
soup = BeautifulSoup(html_text.text,'html.parser')
countries = soup.find_all('div',class_='col-md-4 country')

for country in countries:
    country_name = country.find('h3',class_='country-name').text
    capital = country.find('span',class_='country-capital').text
    population = country.find('span',class_='country-population').text
    area = country.find('span',class_='country-area').text

    nations_info={'Country': country_name.strip(),'Capital': capital.strip(),'Population': population.strip(), 'Area': area.strip()}

    WorldNations.append(nations_info)

print('Total Countries:',len(WorldNations))
df = pd.DataFrame(WorldNations)
print(df.head())
