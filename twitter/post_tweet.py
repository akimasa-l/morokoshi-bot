import json
import requests
import prettier
import credentials

def tweet(message):
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": "【TLから学ぶもろこしbot】\n"+prettier.escape_output(message)}
    response = requests.post(url, params=params, auth=credentials.AUTH)
    print(response.status_code)
    print(json.dumps(json.loads(response.text), indent=4))
