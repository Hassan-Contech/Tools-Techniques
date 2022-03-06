import urllib.request
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup 
import csv

base_url = 'https://www.thestar.com.my/search/?q=Covid&qsort=oldest&qrec=10&qstockcode=&pgno='
url_list = ["{}{}".format(base_url, str(page)) for page in range(1, 408)]
s=[]
open('./Assignment12/dataScapping.csv','w')

for url in url_list:
    s.append(url)
    
for pg in s:
    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(pg)
    try:
        search_response = urllib.request.urlopen(pg)
    except urllib.request.HTTPError:
        pass
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    # Take out the <div> of name and get its value
    ls = [x.get_text(strip=True) for x in soup.find_all("h2", {"class": "f18"})]
    # save the data in tuple
    print("\nAdding all headers to the file: " + str(ls))
    with open('./Assignment12/dataScapping.csv ','a') as file:
        doc = csv.writer(file, lineterminator='\n\n')
        doc.writerow(ls)
