#/usr/bin/python3

from collections import OrderedDict
import json
import os
from pathlib import Path
import shutil
import time

import tool

FILE = Path(__file__).resolve()
REPO = FILE.parents[1]

# --

try:
    shutil.rmtree(REPO / 'People/Member', ignore_errors=True)
except:
    pass
finally:
    time.sleep(1)
    os.mkdir(REPO / 'People/Member')

try:
    shutil.rmtree(REPO / 'People/Alumni', ignore_errors=True)
except:
    pass
finally:
    time.sleep(1)
    os.mkdir(REPO / 'People/Alumni')

# --

with open(REPO / 'people.json', encoding='utf-8') as fp:
    data = json.loads(fp.read())

data = {int(k):v for k, v in data.items()}
data = sorted(data.items(), key=lambda x: (x[1]["name"]["first"], x[1]["name"]["second"]))
data = OrderedDict(data)

# --

member = tool.Member(data)

member.create_member_page()
member.create_member_pages()

member.create_alumni_page()
member.create_alumni_pages()
