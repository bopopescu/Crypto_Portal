import requests
import json
from datetime import datetime
api_req = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=628da1c052e745c7a577c25bfc504d49")
api = json.loads(api_req.content.decode('utf-8'))

api_req_coins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=2000")
api_coins = json.loads(api_req_coins.content.decode('utf-8'))


class CoinsClass:

    def __init__(self):
        self.coins_id = []
        self.coins_name = [" Select a coin "]

        for item in api_coins:
            self.coins_name.append(item['name'])
            self.coins_id.append(item['id'])

    def ret_name_list(self):
        return self.coins_name

    def ret_id(self, _name):
        for item in api_coins:
            if item['name'] == _name:
                return item['id']

        if _name ==" Select a coin ":
            return "ethereum"

    def ret_rank(self, _id):
        self.rank = "-1"
        for item_ in api_coins:
            if item_['id'] == _id:
                self.rank = item_['rank']

        if self.rank == "-1":
            self.rank = "Null"

        return self.rank

    def re_name(self, _id):
        self.name = "-1"
        for item_ in api_coins:
            if item_['id'] == _id:
                self.name = item_['name']

        if self.name == "-1":
            self.name = "Null"

        return self.name

    def re_timestamp(self, _id):
        self.market = "-1"
        for item_ in api_coins:
            if item_['id'] == _id:
                ts = int(item_['last_updated'])
                self.market = str(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


        if self.market == "-1":
            self.market = "Null"

        return self.market

    def re_market(self, _id):
        self.timestamp = "-1"
        for item_ in api_coins:
            if item_['id'] == _id:
                self.timestamp = item_['price_usd']

        if self.timestamp == "-1":
            self.timestamp = "Null"

        return self.timestamp


class ArticlesClass:
    def __init__(self):
        self.titles_list = []
        self.source_list = []
        self.author_list = []
        self.url_list = []
        self.description_list = []
        for i in range(0,5):
            self.titles_list.append(api["articles"][i]["title"])
            self.source_list.append(api["articles"][i]["source"]["name"])
            self.author_list.append(api["articles"][i]["author"])
            self.description_list.append(api["articles"][i]["description"])
            self.url_list.append(api["articles"][i]["url"])

    def tittle_source(self):
        return self.titles_list

    def author_source(self):
        return self.author_list

    def articles_source(self):
        return self.source_list

    def description_source(self):
        return self.description_list

    def url_source(self):
        return self.url_list
