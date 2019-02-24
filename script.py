import urllib.request as fetch
from bs4 import BeautifulSoup
import csv

url = 'scrape a site'
# Fallback if site only allows browsers to access page - create Request
req = fetch.Request(url, headers={'User-Agent' : "Magic Browser"})
# HTTP Response
response = fetch.urlopen(req)
# cextract body
raw_html = response.read()
# create soup to scrape contents
soup = BeautifulSoup(raw_html, 'html.parser')

# do something with the soup ! - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
