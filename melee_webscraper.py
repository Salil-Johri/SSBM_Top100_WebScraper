import csv
import requests
from bs4 import BeautifulSoup
url = "https://liquipedia.net/smash/SSBMRank"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('tbody')

list_of_rows = []
for row in table.findAll('tr'):
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.encode('utf-8').strip()
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)


print list_of_rows
outfile = open("players.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Seed", "kappa", "Name", "omegalul", "score"])
writer.writerows(list_of_rows)