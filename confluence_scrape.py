from bs4 import BeautifulSoup
import requests
import csv
import lxml
import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

source = requests.get('https://cs.stanford.edu/directory/faculty').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'phone', 'office', 'email'])

for tr in soup.find_all('tr')[1:]:
    tds=tr.find_all('td')
    name=cleanhtml(tds[0].encode('utf-8'))
    phone=cleanhtml(tds[1].encode('utf-8'))
    office=cleanhtml(tds[2].encode('utf-8'))
    email=cleanhtml(tds[3].encode('utf-8'))
    email=email+'@cs.stanford.edu'
    # name=lxml.html.fromstring(name).text_content()
    # phone=lxml.html.fromstring(phone).text_content()
    # office=lxml.html.fromstring(office).text_content()
    # email=lxml.html.fromstring(email).text_content()
    print 'name: %s, phone: %s, office: %s, email: %s' %(name, phone, office, email)
    print type(name), type(phone), type(office), type(email)
    csv_writer.writerow([name, phone, office, email])
# csv_writer.close()
