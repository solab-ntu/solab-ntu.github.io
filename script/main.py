from collections import OrderedDict
import json
import os
import shutil
import time

import tool

# --

try:
    shutil.rmtree('../People/Member', ignore_errors=True)
except:
    pass
finally:
    time.sleep(1)
    os.mkdir('../People/Member')

try:
    shutil.rmtree('../People/Alumni', ignore_errors=True)
except:
    pass
finally:
    time.sleep(1)
    os.mkdir('../People/Alumni')

# # --

with open('people.json', encoding='utf-8') as fp:
    data = json.loads(fp.read())

data = {int(k):v for k, v in data.items()}
data = sorted(data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"]))
data = OrderedDict(data)

# # --

tool.page.create_member_page(data)
tool.page.create_member_pages(data)

tool.page.create_alumni_page(data)
tool.page.create_alumni_pages(data)
