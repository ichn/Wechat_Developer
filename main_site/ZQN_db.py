import json
import os
import cloudant
from cloudant.client import Cloudant

class zqn_db:
    def __init__(self):
        env = json.loads(os.getenv("VCAP_SERVICES"))

        username = env["cloudantNoSQLDB"][0]["credentials"]["username"]
        password = env["cloudantNoSQLDB"][0]["credentials"]["password"]
        host = env["cloudantNoSQLDB"][0]["credentials"]["host"]
        url = env["cloudantNoSQLDB"][0]["credentials"]["url"]
        port = int(env["cloudantNoSQLDB"][0]["credentials"]["port"])

        client = Cloudant(username, password, host=host, url=url, port=port, )
        client.connect()

        self.db = client["test_db"]

    def q_by_id(self, id):
        selector = {
            "wechat_id": id,
            "eve_type": "morning"
        }
        fields = [
            "eve_time"
        ]
        res = self.db.get_query_result(selector=selector, fields=fields)
        timestamp = []
        for doc in res:
            timestamp.append(doc['eve_time'])
        return timestamp

    def q_by_id_itv(self, id, a, b):
        selector = {
            "wechat_id": id,
            "eve_type": "morning",
            "eve_time": {
                "$gt": a,
                "$lt": b
            }
        }
        fields = [
            "eve_time"
        ]
        res = self.db.get_query_result(selector=selector, fields=fields)
        timestamp = []
        for doc in res:
            timestamp.append(doc['eve_time'])
        return timestamp

    def q_by_itv(self, a, b):
        selector = {
            "eve_type": "morning",
            "eve_time": {
                "$gt": a,
                "$lt": b
            }
        }
        fields = [
            "eve_time"
        ]
        res = self.db.get_query_result(selector=selector, fields=fields)
        timestamp = []
        for doc in res:
            timestamp.append(doc['eve_time'])
        return timestamp

    def add_eve(self, name, wechat_id, eve_type, eve_time, rnk):
        data = {}
        data["name"] = name
        data["wechat_id"] = wechat_id
        data["eve_type"] = eve_type
        data["eve_time"] = eve_time
        data["rnk"] = rnk
        #print data
        self.db.create_document(data)
