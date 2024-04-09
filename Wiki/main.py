import requests
from bs4 import BeautifulSoup

topic = input(">>> ").replace(' ','_')
URL = f"https://en.wikipedia.org/wiki/{topic}"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
print(''.join(soup.find_all('p')[0].get_text()))