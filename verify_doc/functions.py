import pandas as pandas
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import lxml

# %matplotlib inline

from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrapper(doc_reg):
	url = 'http://medicalboard.co.ke/online-services/retention/?currpage={}'
	page = 0
	
	
	while True:
		try:
			current_page = url.format(page)
			target_page = urlopen(current_page)
			soup = BeautifulSoup(target_page, 'lxml')
			# print(soup.title)
			main_div = soup.find('div', attrs={"id":'main'})
			# print(main_div)
			table = main_div.find('table', attrs={"class":'zebra'})
			table_body = table.find('tbody')
			rows = table_body.find_all('tr')[:10]
			# numbers = []

			for row in rows:
				if doc_reg == row.find_all('td')[2].get_text():
					return "found"
				else:
					return "not found"
		except Exception as e:
			print(e)
			break
		page += 1
	
# if __name__ == '__main__':
# 	print(scrapper('C'))
				
