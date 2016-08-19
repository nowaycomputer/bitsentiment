from pymongo import MongoClient
import requests
import bitcoin_data_scrapers as bcs
import database as db


cb_scraper=bcs.Coinbase_Scraper()
price_database=db.Mongo_Database()
price_database.store_single(cb_scraper.get_spot_price())
