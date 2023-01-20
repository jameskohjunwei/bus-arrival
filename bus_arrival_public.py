import json
import urllib
from urllib.parse import urlparse
import httplib2 as http #External library
from datetime import datetime
from datetime import timezone
from dateutil import tz
import requests

def send_telegram(stored_messages):
    base_url = 'insert your tele api link here'.format(a=stored_messages)
    requests.get(base_url)

#Authentication parameters
headers = { 'AccountKey' : 'insert account key here get it from lta data mall','accept' : 'application/json'} #this is by default

#API parameters
uri = 'http://datamall2.mytransport.sg' #Resource URL
path = '/ltaodataservice/BusArrivalv2?BusStopCode=81111&ServiceNo=155'

#Build query string & specify type of API call
target = urlparse(uri + path)
print(target.geturl())
method = 'GET'
body = ' '

#Get handle to http
h = http.Http()

#Obtain results
response, content = h.request(target.geturl(),method,body,headers)

#  Parse JSON to print
jsonObj = json.loads(content)
# print(json.dumps(jsonObj, sort_keys=True, indent=4))

target_bus_arrival = jsonObj["Services"][0]["NextBus"]["EstimatedArrival"]
target_bus_arrival_time = datetime.fromisoformat(f"{target_bus_arrival}")
now_time = datetime.now()


difference = target_bus_arrival_time.replace(tzinfo=now_time.tzinfo) - now_time
stored_messages = str("bus 155 arriving at payalebarmrt in {t}".format(t=difference))
print(stored_messages)

send_telegram(stored_messages)