import requests
import json

api_req=requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=628da1c052e745c7a577c25bfc504d49")
api=json.loads(api_req.content.decode('utf-8'))

def data_function():
	titles_list = []
	source_list = []
	author_list = []
	url_list = []
	description_list = []
	for i in range(0,5):
		titles_list.append(api["articles"][i]["title"])
		source_list.append(api["articles"][i]["source"]["name"])
		author_list.append(api["articles"][i]["author"])
		description_list.append(api["articles"][i]["description"])
		url_list.append(api["articles"][i]["url"])
	return titles_list,source_list,author_list,description_list,url_list

titles_list,source_list,author_list,description_list,url_list = data_function()

def  tittle_source():
	return titles_list

def author_source():
	return author_list

def articles_source():
	return source_list

def description_source():
	return description_list

def url_source():
	return url_list
