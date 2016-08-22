import requests

class Coinbase_Scraper:
	
	def __init__(self):
		self.source='https://coinbase.com/api/v1/prices/spot_rate'
	
	def get_spot_price(self):
		r  = requests.get(self.source)
		return r.json()

