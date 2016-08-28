from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime
import requests
import re
import database as db

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
    
	def get_data(self,url):
			print 'Processing News story'
			r  = requests.get(url)
			# Get story text
			data = r.text
			soup = BeautifulSoup(data,"lxml")
			# Structure data
			return {'type':'news_story','url':url,'body':soup.getText(),
                        'retrieved':datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S")}

class Finviz_Scraper:
    
	def __init__(self):
		self.source='http://www.finviz.com/news.ashx'
		self.datab=db.Mongo_Database()
		
	def get_finviz_news(self):
		r  = requests.get(self.source)
		data = r.text
		soup = BeautifulSoup(data,"lxml")
		text=""
		for link in soup.find_all("a", {"class" : "nn-tab-link"}):
            # check if valid link
			if self.is_valid_URL(link.get('href')):
				if self.is_parseable(link.get('href')):
                    # check if link is already in the DB, we only want new links
					if self.datab.is_new_story(link.get('href')):
						print(link.contents[0].encode('utf-8'))
						self.datab.store_single({'type':'news_story','url':link.get('href'),'body':self.news_parser(link.get('href')).decode('utf-8','ignore').encode("utf-8"), 'retrieved':datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S")})
                        
	def news_parser(self,url):
		#print(url)
		ctext=""
		if "http://" in url:
			req=requests.get(url)
			data=req.text
			soup=BeautifulSoup(data,"lxml")
			if "reuters.com" in url:
				articleText = soup.find('span', {'id': 'articleText'})
			elif "bloomberg.com" in url:
				articleText = soup.find('div', {'class': 'article-body__content'})
			elif "marketwatch.com" in url:
				articleText = soup.find('div', {'id': 'article-body'})
			elif "yahoo.com" in url:
				articleText = soup.find('div', {'class': 'body yom-art-content clearfix'})
			elif "businessinsider" in url:
				articleText = soup.find('div', {'class': 'KonaBody post-content'})
			if (articleText is not None):
				text=re.sub('\s+', ' ', articleText.text)
				text.strip(' \t\n\r')
				return text.encode('latin-1','replace')
			else:
				return ""

	def is_valid_URL(self,url):
		if url.startswith("http"):
			return True
		else:
			return False

	def is_parseable(self,url):
		list=['reuters.com','bloomberg.com','marketwatch.com','yahoo.com','businessinsider.com']
		for site in list:
			if site in url:
				return True
        
                        