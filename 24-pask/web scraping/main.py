from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
wik = response.text

soup = BeautifulSoup(wik, 'html.parser')

wik_project = soup.select(selector = '#sister-projects-list li .extiw')
wiki_normalized = []


for projects in wik_project:
    print(projects)
    wiki_normalized.append(projects.getText())


print(wiki_normalized)
