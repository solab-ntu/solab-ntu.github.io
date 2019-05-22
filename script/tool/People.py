"""
demo["name"]["chi"] = None
demo["name"]["eng"] = None
demo["year"] = None
demo["lab_id"] = None
demo["alumni"] = True
demo["thesis"] = {"chi": None, "eng": None, "file": None, "drive": None}
demo["degrees"][id] = {"chi": None, "eng": None}
demo["jobs"][id] = {"chi": None, "eng": None, "web": None}
demo["papers"][id] = {"ref": None, "file": None, "drive": None, "type": None, "year": None}
demo["degrees"][id] = {id: {"chi": None, "eng": None}
"""

class People(dict):

    def __init__(self):

        self["name"] = {"chi": None, "eng": None, "first": None, "second": None, "weight": None}
        self["lab_id"] = None
        self["alumni"] = True
        self["year"] = None
        self["jobs"] = dict() # {id: {"chi": None, "eng": None, "web": None}, ...}
        self["thesis"] = {"chi": None, "eng": None, "file": None, "drive": None}
        self["research"] = {"chi": None, "eng": None}
        self["papers"] = dict() # {id: {"ref": None, "file": None, "drive": None, "type": None, "year": None}, ...}
        self["show_paper"] = True
        self["degrees"] = dict() # {id: {"chi": None, "eng": None}, ...}

    def set_first_second(self):

        self["name"]["second"], self["name"]["first"] = self["name"]["eng"].split(" ")
