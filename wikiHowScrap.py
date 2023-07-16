#!/usr/bin/env python3

from termcolor import colored
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re


#Ask for user input
how = colored('How','yellow')
wiki = colored('Wiki','green')
print((f'\n{wiki}{how}'), colored('WebScrapper', 'cyan'))


print('Introduce término a buscar: \n')
url = f"https://es.wikihow.com/wikiHowTo?search={input().replace(' ','+')}"
print(url)


#string = re.sub(r"\s*{.*}\s*", " ", string)


#Get HTML
client = urlopen(url)
html = client.read()
client.close()
soup = BeautifulSoup(html, 'html.parser')


#Get link
searchResults = soup.find('div', attrs = {'id':'searchresults_list'})
links = searchResults.find('a', attrs = {'class':'result_link'})
link = links.get('href')


print(f'{link} \n')


#Get HTML
client = urlopen(link)
html = client.read().decode('utf8')
client.close()
soup = BeautifulSoup(html, 'html.parser')


data = []


#Get article
steps = soup.findAll('div', attrs = {'class':'step'})


for step in steps:
	step = re.sub(r"\[[0-9]+\]XFuente de investigación", "", step.get_text().replace('\n', ''))
	data.append(re.sub(r"\s*{.*}\s*", " ", step))
for d in data:
	print(f'\n{d}')
