import json
import os
import shutil

import web_tool

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

with open('people.json', encoding='utf-8') as fp:
    data = json.loads(fp.read())

data = {int(k):v for k, v in data.items()}

web_tool.page.create_member(data)
web_tool.page.create_current(data)
web_tool.page.create_member_page(data)
web_tool.page.create_alumni(data)
web_tool.page.create_alumni_page(data)
