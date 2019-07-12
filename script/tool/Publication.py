import os
import codecs
from . import template

class Publication():

    def __init__(self, data):

        self.journal = []
        self.inter_conf = []
        self.domes_conf = []

        for k1, v1 in data.items():
            if v1["papers"]:
                for k2, v2 in v1["papers"].items():
                    if v2["type"] == "j" and v2 not in self.journal: # journal
                        self.journal.append(v2)
                    elif v2["type"] == "ic" and v2 not in self.inter_conf: # international conference
                        self.inter_conf.append(v2)
                    elif v2["type"] == "dc" and v2 not in self.domes_conf: # domestic conference
                        self.domes_conf.append(v2)
                    else:
                        pass
            else:
                pass

    def sort(self):

        self.journal.sort(key=lambda x: x["year"])
        self.inter_conf.sort(key=lambda x: x["year"])
        self.domes_conf.sort(key=lambda x: x["year"])

    def create_page(self):
        
        script = ""
        script += template.Publication.script1

        for i in reversed(self.journal):
            ref = i["ref"]
            drive = i["drive"]
            if drive == "":
                script += template.Publication.script2_1.format(ref)
            else:
                script += template.Publication.script2_2.format(ref, drive)

        script += template.Publication.script3

        for i in reversed(self.inter_conf):
            ref = i["ref"]
            drive = i["drive"]
            if drive == "":
                script += template.Publication.script2_1.format(ref)
            else:
                script += template.Publication.script2_2.format(ref, drive)

        script += template.Publication.script4

        for i in reversed(self.domes_conf):
            ref = i["ref"]
            drive = i["drive"]
            if drive == "":
                script += template.Publication.script2_1.format(ref)
            else:
                script += template.Publication.script2_2.format(ref, drive)

        script += template.Publication.script5

        with codecs.open('../Publication/Publication.html', "w", encoding='utf8') as file:
            file.write(script)
            file.close()