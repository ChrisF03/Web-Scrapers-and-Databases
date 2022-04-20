from bs4 import BeautifulSoup
import requests
import pandas as pd

books =  []

def getInfo(page):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text,'html.parser')
    site = soup.find_all('article',class_='product_pod')

    for titles in site:
        title = titles.find('h3').text
        rating = titles.find('p').attrs
        stars = rating['class'][1]
        price = titles.find('p',class_='price_color').text

        book_info={'Title': title.strip(),'Star Rating': stars.strip(),'Price': price.strip()}
        books.append(book_info)
    return

for x in range(1,51):
    getInfo(x)
 
df = pd.DataFrame(books)
print(df.shape)
print(df.head())
