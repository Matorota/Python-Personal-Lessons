from bs4 import  BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html")
#print.(soup title.string)

heading = soup.find(name="h1").getText()
print(heading)

name = soup.find(name="p", id='name').getText()
title = soup.find(name='h3', ).getText()

all_tags = soup.findAll(name='a')
print(all_tags)

for tag in all_tags:
    print(tag.getText())
    print(tag.get('href'))

company_url = soup.select_one(selector='p a').get('href')
print(company_url)

all_url = soup.find_all()
