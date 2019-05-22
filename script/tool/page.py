import io
import os
import codecs
from . import template

def create_member_grid(data):

    members = []

    for k in data.keys():
        if data[k]["alumni"] is False:
            members.append(data[k])

    script = template.Member.script1
    col_num = 1

    for d in members:

        name = d["name"]
        path_html = "./" + name["eng"] + ".html"
        path_pic = "../files/" + name["eng"] +".jpg"
        script += template.Member.script2.format(path_html, name["eng"], name["chi"], path_pic)

        if col_num % 4 == 0:
            script += template.Member.script3_1
        else:
            script += template.Member.script3_2
                
        col_num += 1

    return (members, script)

def create_member_page(data):

    _, script = create_member_grid(data)
    script = script + template.Member.script4

    try:
        os.remove("../People/Member/Member.html")
    except OSError:
        pass

    with codecs.open("../People/Member/Member.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_member_pages(data):

    members, script = create_member_grid(data)

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
            os.remove("../People/Member/" + name["eng"] + ".html")
        except OSError:
            pass

        with codecs.open("../People/Member/" + name["eng"] + ".html", "w", encoding='utf8') as file:
            file.write(script_member_page)
            file.close()    

def create_alumni_grid(data):

    alumni = []

    for k in data.keys():
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

    return (alumni, script)

def create_alumni_page(data):

    _, script = create_alumni_grid(data)
    script = script + template.Alumni.script4

    try:
        os.remove("../People/Alumni/Alumni.html")
    except OSError:
        pass

    with codecs.open("../People//Alumni/Alumni.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_alumni_pages(data):

    alumni, script = create_alumni_grid(data)

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
            os.remove("../People/Alumni/" + name["eng"] + ".html")
        except OSError:
            pass

        with codecs.open("../People/Alumni/" + name["eng"] + ".html", "w", encoding='utf8') as file:
            file.write(script_alumni_page)
            file.close()    
