# twitterApi - Twitter Rest API Simplified Client
# author: Julio Vasconez

import json
import requests 
from operator import itemgetter
access_token="YOUR_ACCESS_TOKEN";
iteration_limit=100
iteration_count=0
def getTweets(params):
    global iteration_count
    print("Iteracion "+ str(iteration_count))
    print("Obteniendo Tweets Referentes a "+params["q"]+"...")
    headers={"Authorization":"Bearer "+access_token}
    result = requests.get("https://api.twitter.com/1.1/search/tweets.json",params=params,headers=headers)
    json_result=json.loads(str(result.text))
    return json_result


def getAllTweets(params,lowest_id=0,all_statuses=[]):
	global iteration_count
	global iteration_limit
	iteration_count+=1
	if(lowest_id!=0):
		params["max_id"]=lowest_id-1

	new_response=getTweets(params)
	
	if(len(new_response["statuses"])==0) or iteration_count>=iteration_limit:
		return new_response["statuses"]
	else:
		statuses=new_response["statuses"]
		lowest_id=min(statuses,key=itemgetter("id"))
		return statuses+getAllTweets(params,lowest_id=lowest_id["id"])
	

