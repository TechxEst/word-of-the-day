import requests
import json
import os

url = "https://word-of-the-day2.p.rapidapi.com/word/dc"

headers = {
	"X-RapidAPI-Key": os.environ.get("WOTD_APIKEY"),
	"X-RapidAPI-Host": "word-of-the-day2.p.rapidapi.com"
}

wotd = requests.request("GET", url, headers=headers).json()

def slack_alert(wotd):
    webhook_url = os.environ.get("WOTD_HOOK")
    slack_data = {'text': "Today's word:\n{}\nDefinition:\n{}".format(wotd[0]["word"], wotd[0]["mean"])} 
    requests.post(webhook_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'})

if __name__ == "__main__":
    slack_alert(wotd)