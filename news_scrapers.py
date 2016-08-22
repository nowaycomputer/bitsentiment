from bs4 import BeautifulSoup
from pymongo import MongoClient
from datetime import datetime
import requests

class Twitter_Scraper:
	
	def __init__(self):
		self.source='https://twitter.com/search?f=news&vertical=news&q=bitcoin&src=typd'
	
	def get_twitter_news(self):
		r  = requests.get(self.source)
		list_of_news_urls=[]
		data = r.text
		soup = BeautifulSoup(data,"lxml")
		for link in soup.findAll("a", href=True):
			if 't.co' in link['href']:
				list_of_news_urls.append(link['href'])
		return list_of_news_urls


#https://coinbase.com/api/v1/prices/spot_rate