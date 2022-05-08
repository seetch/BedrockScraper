import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.digminecraft.com/lists/item_id_list_pe.php'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

block_dict = {}

table = soup.find(id="minecraft_items")
rows = table.find_all("tr")

i = 0
for row in rows:
    cells = row.find_all("td")
    block_name = ""
    img_url = ""
    for cell in cells:
        if(cell.find('img')):
            img_url = 'https://www.digminecraft.com' + \
                cell.find('img')['data-src']

        if(cell.find('a')):
            block_name = cell.find('a').text


    if ("Potion" in block_name or "Splash Potion" in block_name or "Arrow of" in block_name):
            continue

    block_dict[block_name] = img_url


with open('ids\\blocks.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'img_url'])
    for key in block_dict:
        writer.writerow([key, block_dict[key]])