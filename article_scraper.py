# As of 30/09/2021, the scraper works on:
# The Japan Times
# The New York Times

from bs4 import BeautifulSoup
import requests

url = input()
article = requests.get(url)

soup = BeautifulSoup(article.content, 'html.parser')
body = soup.find_all("p")

# Provides paragraph tag elements in HTML page 
article = ""
for paragraph in body:
    article += '\n' + str(paragraph)

# Provides raw text article for stdout
raw_article = ""
for paragraph in body:
    raw_article += '\n\n' + paragraph.find(text = True)

print("Raw text: \n" + raw_article)

file = open("article.html", "w", encoding='utf-8')
file.write("<head><style> p { margin: 32px 64px; font-size: 20px; font-family: Arial, Helvetica, sans-serif; } </style></head>")
file.write(article)
file.close()

