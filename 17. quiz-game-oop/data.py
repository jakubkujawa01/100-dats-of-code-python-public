import urllib.request
import json

url = "https://opentdb.com/api.php?amount=12&difficulty=easy&type=boolean"

data = urllib.request.urlopen(url).read()

question_data = json.loads(data)["results"]
