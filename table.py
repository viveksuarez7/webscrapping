import requests 

import csv

from bs4 import BeautifulSoup as bs
import urllib3
urllib3.disable_warnings()


url = requests.get("https://dubaimerc.com/trading-hours-and-holiday-calendar",verify=False)
soup = bs(url.content,'html.parser')
filename = 'test.csv'
csv_writer = csv.writer(open(filename,'w'))
table= soup.find('table',class_='table')


# run a  loop to extaract the table data and store it in csv file


for tr in soup.find_all('tr'):
    data=[]
    
    # for extracting the table heading ..... 

    for th in tr.find_all('th'):
        data.append(th.text.strip())
    

    if(data):
        print('Headers : {}'.format(','.join(data)))
        csv_writer.writerow(data)
        continue

# # for scrapping table data values

    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if(data):
        print("Insert Table Data: {}".format(",".join(data)))
        csv_writer.writerow(data)



