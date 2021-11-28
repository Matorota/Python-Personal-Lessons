from bs4 import BeautifulSoup
import requests


response = requests.get('https://www.1a.lt/c/kompiuterine-technika-biuro-prekes/monitoriai-stacionarus-kompiuteriai-ir-ups/monitoriai/2t6')
shop = response.text


soup = BeautifulSoup(shop, 'html.parser')

monitors_price = soup.select( selector = '.catalog-taxons-product-price__item-price')
monitors_price_normalized = []
# monitors_price_normalized.select_one(":nth-child(1)")


for projects in monitors_price:
    print(monitors_price_normalized)
    monitors_price_normalized.append(projects.getText())

# rows = monitors_price_normalized.findAll('span')[0::1]

print(monitors_price_normalized)
