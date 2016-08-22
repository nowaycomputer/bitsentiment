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
tw_scraper=ns.Twitter_Scraper()

# repeat every minute, forever
while True:
	# Get list of stories
	twitter_stories=tw_scraper.get_twitter_news()
	# Get bitcoin price
	btc_data={'type': 'btc_usd_rate','source':'https://coinbase.com/api/v1/prices/spot_rate','timestamp':datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S"),'data':cb_scraper.get_spot_price()}
	# Store data
	datab.store_single(btc_data)
	# For each story
	for url in twitter_stories:
		# Check if it's already in DB (based on URL)
		if not datab.check_if_story_exists:
			r  = requests.get(url)
			# Get story text
			data = r.text
			soup = BeautifulSoup(data,"lxml")
			# Structure data
			story_data={'type':'news_story','url':url,'body':soup.getText(),'retrieved':datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S")}
			# Store in the DB
			datab.store_single(story_data)
	time.sleep(60)