import os
import shutil

import web_tool

try:
    os.remove('Member.html')
    shutil.rmtree('Member', ignore_errors=True)
    shutil.rmtree('Alumni', ignore_errors=True)
except:
    pass
finally:
    os.mkdir('Alumni')
    os.mkdir('Member')

web_tool.page.create_member('Member.tsv')
web_tool.page.create_current('Member.tsv')
web_tool.page.create_member_page('Member.tsv')
web_tool.page.create_alumni('Alumni.tsv')
web_tool.page.create_alumni_page('Alumni.tsv')
