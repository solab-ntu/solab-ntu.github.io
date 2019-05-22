from collections import OrderedDict
import json
import os

import tool

# --

try:
    os.remove('../Publication/Publication.html')
except:
    pass

# --

with open('people.json', encoding='utf-8') as fp:
    data = json.loads(fp.read())

data = {int(k):v for k, v in data.items()}
data = sorted(data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"]))
data = OrderedDict(data)

# --

pubs = tool.Publication(data)
pubs.sort()
pubs.create_page()