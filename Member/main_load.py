import json

from web_tool import member

with open('people.json', encoding='utf-8') as fp:
    data = json.loads(fp.read())

data = {int(k):v for k, v in data.items()}
