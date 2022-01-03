from bs4 import BeautifulSoup as bs
import requests
import wget

DOMAIN = 'https://www.spglobal.com'
URL = 'https://www.spglobal.com/platts/en/our-methodology/holiday'
FILETYPE = '.xls'

def get_soup(url):
    return bs(requests.get(url).text,'html.parser')

for link in get_soup(URL).find_all('a',class_='link'):
    file_link=link.get('href')
    if FILETYPE in file_link:
        print(file_link)
        with open(link.text,'wb') as file:
            response=requests.get(DOMAIN + file_link)
            file.write(response.content)