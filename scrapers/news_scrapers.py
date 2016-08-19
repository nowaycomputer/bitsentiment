# Twitter base news URL

# https://twitter.com/search?f=news&vertical=news&q=bitcoin&src=typd
from pymongo import MongoClient
from datetime import datetime
import requests

client = MongoClient()
db = client.test



#https://coinbase.com/api/v1/prices/spot_rate