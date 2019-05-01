import os
import shutil

import member

try:
    os.remove('Member.html')
    shutil.rmtree('Member', ignore_errors=True)
    shutil.rmtree('Alumni', ignore_errors=True)
except:
    pass
finally:
    os.mkdir('Alumni')
    os.mkdir('Member')

member.create_member('Member.tsv')
member.create_current('Member.tsv')
member.create_member_page('Member.tsv')
member.create_alumni('Alumni.tsv')
member.create_alumni_page('Alumni.tsv')
