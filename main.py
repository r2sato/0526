import requests
from bs4 import BeautifulSoup

# Get
res = requests.get('https://qiita.com/')

# Parse
soup = BeautifulSoup(res.text, 'html.parser')

# title
title = soup.find('title').text

print(title)


