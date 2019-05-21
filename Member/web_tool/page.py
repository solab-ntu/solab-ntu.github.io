import io
import re
import os
import codecs
from . import template

def create_member(data):

    members = []

    for k in sorted(data):
        if data[k]["alumni"] is False:
            members.append(data[k])

    script = template.Member.script1
    col_num = 1

    for d in members:

        name = d["name"]
        path_html = "./Member/" + name["eng"] + ".html"
        path_pic = "./files/" + name["eng"] +".jpg"
        script += template.Member.script2.format(path_html, name["eng"], name["chi"], path_pic)

        if col_num % 4 == 0:
            script += template.Member.script3_1
        else:
            script += template.Member.script3_2
                
        col_num += 1

    script = script + template.Member.script4

    try:
        os.remove("Member.html")
    except OSError:
        pass

    with codecs.open("Member.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_current(data):

    members = []

    for k in sorted(data):
        if data[k]["alumni"] is False:
            members.append(data[k])

    script = template.Current.script1
    col_num = 1

    for d in members:

        name = d["name"]
        path_html = "./" + name["eng"] + ".html"
        path_pic = "../files/" + name["eng"] +".jpg"

        script += template.Current.script2.format(path_html, name["eng"], name["chi"], path_pic)

        if col_num % 4 == 0:
            script += template.Current.script3_1
        else:
            script += template.Current.script3_2

        col_num += 1
                
    script += template.Current.script4

    try:
        os.remove("./Member/Current.html")
    except OSError:
        pass

    with codecs.open("./Member/Current.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_member_page(data):

    members = []

    for k in sorted(data):
        if data[k]["alumni"] is False:
            members.append(data[k])

    script = template.Current.script1
    col_num = 1

    for d in members:

        name = d["name"]
        path_html = "./" + name["eng"] + ".html"
        path_pic = "../files/" + name["eng"] +".jpg"

        script += template.Current.script2.format(path_html, name["eng"], name["chi"], path_pic)

        if col_num % 4 == 0:
            script += template.Current.script3_1
        else:
            script += template.Current.script3_2

        col_num += 1
                
    # --

    for d in members:

        script_member_page = script + template.MemberPage.script1

        name = d["name"]
        lab_id = d["lab_id"]
        jobs = d["jobs"]
        degrees = d["degrees"]
        research = d["research"]
        thesis = d["thesis"]
        papers = d["papers"]

        path_pic = "../files/" + name["eng"] +".jpg"
        script_member_page += template.MemberPage.script2_1.format(path_pic, name["chi"], name["eng"], lab_id)

        if jobs:
            tmp = ""
            for k in sorted(jobs):
                tmp += jobs[k]["chi"] + "<br />" + jobs[k]["eng"] + "<br /><br />"
            script_member_page += template.AlumniPage.script2_2_1.format(tmp)

        if degrees:
            tmp = ""
            for k in sorted(degrees):
                tmp += degrees[k]["chi"] + "<br />" + degrees[k]["eng"] + "<br /><br />"
            script_member_page += template.MemberPage.script2_1_1.format(tmp)

        if any(value is not None for value in research.values()):
            script_member_page += template.MemberPage.script2_2.format(research["chi"], research["eng"])

        if any(value is not None for value in thesis.values()):
            script_member_page += template.AlumniPage.script2_4.format(thesis["chi"], thesis["eng"], thesis["drive"])

        if papers:
            script_member_page += template.MemberPage.script3_1
            for k, v in papers.items():
                if v["drive"] == "":
                    script_member_page += template.MemberPage.script3_2.format(v["ref"])
                else:
                    script_member_page += template.MemberPage.script3_3.format(v["ref"], v["drive"])
            
        script_member_page += template.MemberPage.script4
        
        try:
            os.remove("./Member/" + name["eng"] + ".html")
        except OSError:
            pass

        with codecs.open("./Member/" + name["eng"] + ".html", "w", encoding='utf8') as file:
            file.write(script_member_page)
            file.close()    

def create_alumni(data):

    alumni = []

    for k in reversed(sorted(data)):
        if data[k]["alumni"] is True:
            alumni.append(data[k])

    script = template.Alumni.script1
    col_num = 1

    for d in alumni:

        name = d["name"]
        path_html = "./" + name["eng"] + ".html"
        path_pic = "../files/" + name["eng"] +".jpg"
        script += template.Alumni.script2.format(path_html, name["eng"], name["chi"], path_pic)

        if col_num % 4 == 0:
            script = script + template.Alumni.script3_1
        else:
            script = script + template.Alumni.script3_2

        col_num += 1
                
    script = script + template.Alumni.script4

    try:
        os.remove("./Alumni/Alumni.html")
    except OSError:
        pass

    with codecs.open("./Alumni/Alumni.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_alumni_page(data):

    alumni = []

    for k in reversed(sorted(data)):
        if data[k]["alumni"] is True:
            alumni.append(data[k])

    script = template.Alumni.script1
    col_num = 1

    for d in alumni:

        name = d["name"]
        path_html = "./" + name["eng"] + ".html"
        path_pic = "../files/" + name["eng"] +".jpg"
        script += template.Alumni.script2.format(path_html, name["eng"], name["chi"], path_pic)

        if col_num % 4 == 0:
            script = script + template.Alumni.script3_1
        else:
            script = script + template.Alumni.script3_2

        col_num += 1
                
    # --

    for d in alumni:

        script_alumni_page = script + template.MemberPage.script1

        name = d["name"]
        lab_id = d["lab_id"]
        jobs = d["jobs"]
        degrees = d["degrees"]
        research = d["research"]
        thesis = d["thesis"]
        papers = d["papers"]

        path_pic = "../files/" + name["eng"] +".jpg"
        script_alumni_page += template.AlumniPage.script2_1.format(path_pic, name["chi"], name["eng"])

        if jobs:
            tmp = ""
            for k in sorted(jobs):
                script_alumni_page += template.AlumniPage.script2_2.format(jobs[k]["web"], jobs[k]["chi"], jobs[k]["eng"])

        if degrees:
            tmp = ""
            for k in sorted(degrees):
                tmp += degrees[k]["chi"] + "<br />" + degrees[k]["eng"] + "<br /><br />"
            script_alumni_page += template.MemberPage.script2_1_1.format(tmp)

        if any(value is not None for value in research.values()):
            script_alumni_page += template.MemberPage.script2_2.format(research["chi"], research["eng"])

        if any(value is not None for value in thesis.values()):
            script_alumni_page += template.AlumniPage.script2_4.format(thesis["chi"], thesis["eng"], thesis["drive"])

        if papers:
            script_alumni_page += template.MemberPage.script3_1
            for k, v in papers.items():
                if v["drive"] == "":
                    script_alumni_page += template.MemberPage.script3_2.format(v["ref"])
                else:
                    script_alumni_page += template.MemberPage.script3_3.format(v["ref"], v["drive"])

        script_alumni_page += template.AlumniPage.script3

        try:
            os.remove("./Alumni/" + name["eng"] + ".html")
        except OSError:
            pass

        with codecs.open("./Alumni/" + name["eng"] + ".html", "w", encoding='utf8') as file:
            file.write(script_alumni_page)
            file.close()    
