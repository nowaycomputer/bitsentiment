import requests
import datetime

class Coinbase_Scraper:
	
	def __init__(self):
		self.source='https://coinbase.com/api/v1/prices/spot_rate'
	
	def get_spot_price(self):
		r  = requests.get(self.source)
		return r.json()

	def get_data(self):
		return {'type': 'btc_usd_rate','source':'https://coinbase.com/api/v1/prices/spot_rate',
                'timestamp':datetime.datetime.utcnow().strftime("%d/%m/%y %H:%M:%S"),'data':self.get_spot_price()}


