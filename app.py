import requests
import bitcoin_data_scrapers as bcs
import database as db
import json
import news_scrapers as ns
from bs4 import BeautifulSoup
import datetime
import time

# get db
datab=db.Mongo_Database()

# get scrapers
# bitcoin
cb_scraper=bcs.Coinbase_Scraper()
#twitter
#tw_scraper=ns.Twitter_Scraper()
finviz_scraper=ns.Finviz_Scraper()

# repeat every minute, forever
while True:
	# Get list of stories
	# OLD twitter_stories=tw_scraper.get_twitter_news()
	# Get bitcoin price and Store data
	datab.store_single(cb_scraper.get_data())
	# For each story
	#for url in twitter_stories:
		# Check if it's already in DB (based on URL)
		#if datab.is_new_story:
	#		# Store in the DB
	#		datab.store_single(tw_scraper.get_data(url))
	finviz_scraper.get_finviz_news()
	time.sleep(60)
    
    