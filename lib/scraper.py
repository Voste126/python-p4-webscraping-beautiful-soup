from turtle import ht
from bs4 import BeautifulSoup
import requests

#just incase you get a 403 error on forbidden error
headers = {'user-agent': 'my-app/0.0.1'}
#we grab the HTML page we need to use
html = requests.get("https://flatironschool.com/", headers=headers)
doc = BeautifulSoup(html.text, 'html.parser')
#sample part of the part we need to scrap
print(doc.select('.heading-financier'))
