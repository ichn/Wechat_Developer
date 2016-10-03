# Use CouchDB to create a CouchDB client
# from cloudant.client import CouchDB
# client = CouchDB(USERNAME, PASSWORD, url='http://127.0.0.1:5984')
import ZaoqiNiao
import datetime
# Use Cloudant to create a Cloudant client using account
from cloudant.client import Cloudant
import time
USERNAME = "31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix"
PASSWORD = "b7ce2f24742598d7445e309a870dca83a84ec1dc90edd3dc692ca2e3f6d4806f"
URL = "https://31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix:b7ce2f24742598d7445e309a870dca83a84ec1dc90edd3dc692ca2e3f6d4806f@31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix.cloudant.com"

client = Cloudant(USERNAME, PASSWORD, host="31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix.cloudant.com", url=URL, port=443,)
# or using url
# client = Cloudant(USERNAME, PASSWORD, url='https://acct.cloudant.com')

# Connect to the server
client.connect()

selector = {
    "wechat_id": "sdfxcsdf2sdf1",
    "eve_type": "morning",
    "eve_time": {
      "$gt": 1475383784,
      "$lt": 1475383788
    }
}

field = {
    "eve_time"
}

test_db = client["test_db"]

res = test_db.get_query_result(selector, field)

for doc in res:
    print doc

"""
test_db = client.create_database('test_db')
if test_db.exists():
    print "success"
"""


"""
test_db = client['test_db']

data = {
    "name": "zhzhzh23233",
    "eve_type": "morning",
}

for j in range(1, 11):
    for i in range(1, 11):
        data["name"] = "www" + str(i)
        data["wechat_id"] = "sdfxcsdf2sdf" + str(j)
        data["eve_time"] = int(time.time())
        time.sleep(0.1)
        test_db.create_document(data)
"""



# Perform client tasks...
session = client.session()
print 'Username: {0}'.format(session['userCtx']['name'])
print 'Databases: {0}'.format(client.all_dbs())

# Disconnect from the server
client.disconnect()

"""
{
  "username": "31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix",
  "password": "b7ce2f24742598d7445e309a870dca83a84ec1dc90edd3dc692ca2e3f6d4806f",
  "host": "31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix.cloudant.com",
  "port": 443,
  "url": "https://31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix:b7ce2f24742598d7445e309a870dca83a84ec1dc90edd3dc692ca2e3f6d4806f@31a28f48-fad6-42c0-9d0b-9935659c8b1c-bluemix.cloudant.com"
}
"""
