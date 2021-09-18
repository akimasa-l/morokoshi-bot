import prettier
import json
import requests
import credentials
params = {"count": 200}
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response = requests.get(url, params=params, auth=credentials.AUTH)
timelines = json.loads(response.text)
for timeline in timelines:
    print(prettier.escape_input(timeline["text"]))
