from collections import OrderedDict
import json
import os
import shutil

import web_tool

# --

try:
    os.remove('Member.html')
except:
    pass

try:
    shutil.rmtree('Member', ignore_errors=True)
except:
    pass
finally:
    os.mkdir('Member')

try:
    shutil.rmtree('Alumni', ignore_errors=True)
except:
    pass
finally:
    os.mkdir('Alumni')

# --

with open('people.json', encoding='utf-8') as fp:
    data = json.loads(fp.read())

data = {int(k):v for k, v in data.items()}
data = sorted(data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"]))
data = OrderedDict(data)

# --

web_tool.page.create_member_page(data)
web_tool.page.create_member_pages(data)

web_tool.page.create_alumni_page(data)
web_tool.page.create_alumni_pages(data)
