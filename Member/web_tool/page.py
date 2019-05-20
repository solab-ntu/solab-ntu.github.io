import io
import re
import os
import codecs
from . import template

def create_member(ppl_member_tsv):

    with io.open(ppl_member_tsv, "r", encoding='utf8') as file:
        lines = file.readlines()

    script = template.Member.script1

    col_num = 0 # each row can only show 4 people

    for i in range(1, len(lines)):

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]
        
        col_num += 1
        path_html = "./Member/" + name_eng + ".html"
        path_pic = "./files/" + name_eng +".jpg"

        script += template.Member.script2.format(path_html, name_eng, name_chi, path_pic)

        if col_num % 4 == 0:
            script += template.Member.script3_1
        else:
            script += template.Member.script3_2
                
    script = script + template.Member.script4

    try:
        os.remove("Member.html")
    except OSError:
        pass

    with codecs.open("Member.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_current(ppl_member_tsv):

    with io.open(ppl_member_tsv, "r", encoding='utf8') as file:
        lines = file.readlines()

    script = template.Current.script1

    col_num = 0

    for i in range(1, len(lines)):

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]
        
        col_num += 1
        path_html = "./" + name_eng + ".html"
        path_pic = "../files/" + name_eng +".jpg"

        script += template.Current.script2.format(path_html, name_eng, name_chi, path_pic)

        if col_num % 4 == 0:
            script += template.Current.script3_1
        else:
            script += template.Current.script3_2
                
    script += template.Current.script4

    try:
        os.remove("./Member/Current.html")
    except OSError:
        pass

    with codecs.open("./Member/Current.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_member_page(ppl_member_tsv):

    with io.open(ppl_member_tsv, "r", encoding='utf8') as file:
        lines = file.readlines()

    script = template.Current.script1

    col_num = 0

    for i in range(1, len(lines)):

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]
        
        col_num += 1
        path_html = "./" + name_eng + ".html"
        path_pic = "../files/" + name_eng +".jpg"

        script += template.Current.script2.format(path_html, name_eng, name_chi, path_pic)

        if col_num % 4 == 0:
            script += template.Current.script3_1
        else:
            script += template.Current.script3_2
                
    # --

    for i in range(1, len(lines)):

        script_member_page = script + template.MemberPage.script1

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]

        path_pic = "../files/" + name_eng +".jpg"
        education = education.replace(r"/", "<br /><br />")
        education = education.replace(r"\n", "<br />")

        script_member_page += template.MemberPage.script2_1.format(path_pic, name_chi, name_eng, note)

        if company_chi != "-":
            company_chi = company_chi.replace(r"/", "<br /><br />")
            company_chi = company_chi.replace(r"\n", "<br />")
            script_member_page += template.AlumniPage.script2_2_1.format(company_chi)
            script_member_page += "<br />"

        script_member_page += template.MemberPage.script2_1_1.format(education)

        if thesis_eng != "-":
            if thesis_file == "-":
                script_member_page += template.MemberPage.script2_2.format(thesis_chi, thesis_eng)
            else:
                # path_thesis = "../../Publications/Thesis/" + thesis_file + ".pdf"
                path_thesis = thesis_file
                script_member_page += template.AlumniPage.script2_4.format(path_thesis, thesis_chi, thesis_eng)

        if papers != "-":
            script_member_page += template.MemberPage.script3_1
            papers = papers.split(";")
            papers_file = papers_file.split(";")

            for paper, paper_file in zip(papers, papers_file):
                author, article, tail = paper.split('"')
                # paper_file = "../../Publications/Papers/" + paper_file + ".pdf"
                paper_file = paper_file
                script_member_page += template.MemberPage.script3_2.format(author, article, tail, paper_file)
            
        script_member_page += template.MemberPage.script4
        
        try:
            os.remove("./Member/" + name_eng + ".html")
        except OSError:
            pass

        with codecs.open("./Member/" + name_eng + ".html", "w", encoding='utf8') as file:
            file.write(script_member_page)
            file.close()    

def create_alumni(ppl_alumni_tsv):

    with io.open(ppl_alumni_tsv, "r", encoding='utf8') as file:
        lines = file.readlines()

    lines.reverse()

    script = template.Alumni.script1

    col_num = 0

    for i in range(0, len(lines)-1):

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]
        
        col_num += 1
        path_html = "./" + name_eng + ".html"
        path_pic = "../files/" + name_eng +".jpg"

        script += template.Alumni.script2.format(path_html, name_eng, name_chi, path_pic)

        if col_num % 4 == 0:
            script = script + template.Alumni.script3_1
        else:
            script = script + template.Alumni.script3_2
                
    script = script + template.Alumni.script4

    try:
        os.remove("./Alumni/Alumni.html")
    except OSError:
        pass

    with codecs.open("./Alumni/Alumni.html", "w", encoding='utf8') as file:
        file.write(script)
        file.close()

def create_alumni_page(ppl_alumni_tsv):

    with io.open(ppl_alumni_tsv, "r", encoding='utf8') as file:
        lines = file.readlines()

    lines.reverse()

    script = template.Alumni.script1

    col_num = 0

    for i in range(0, len(lines)-1):

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]
        
        col_num += 1
        path_html = "./" + name_eng + ".html"
        path_pic = "../files/" + name_eng +".jpg"

        script += template.Alumni.script2.format(path_html, name_eng, name_chi, path_pic)

        if col_num % 4 == 0:
            script = script + template.Alumni.script3_1
        else:
            script = script + template.Alumni.script3_2
                
    # --

    for i in range(0, len(lines)-1):

        script_alumni_people = script + template.AlumniPage.script1

        data_list = re.split("""\t""", lines[i])
        
        name_chi    = data_list[1]
        name_eng    = data_list[2]
        note        = data_list[3]
        education   = data_list[4]
        company_chi = data_list[5]
        company_eng = data_list[6]
        company_web = data_list[7]
        thesis_chi  = data_list[8]
        thesis_eng  = data_list[9]
        thesis_file = data_list[11]
        papers      = data_list[12]
        papers_file = data_list[14]

        path_pic = "../files/" + name_eng +".jpg"
        education = education.replace(r"/", "<br /><br />")
        education = education.replace(r"\n", "<br />")
        path_thesis = "../../Publications/Thesis/" + thesis_file + ".pdf"

        script_alumni_people += template.AlumniPage.script2_1.format(path_pic, name_chi, name_eng)

        if company_chi != "-":
            script_alumni_people += template.AlumniPage.script2_2.format(company_web, company_chi, company_eng)

        script_alumni_people += template.AlumniPage.script2_3.format(education)

        if thesis_eng != "-":
            if thesis_file == "-":
                script_alumni_people += template.MemberPage.script2_2.format(thesis_chi, thesis_eng)
            else:
                # path_thesis = "../../Publications/Thesis/" + thesis_file + ".pdf"
                path_thesis = thesis_file
                script_alumni_people += template.AlumniPage.script2_4.format(path_thesis, thesis_chi, thesis_eng)

        if papers != "-":
            script_alumni_people += template.MemberPage.script3_1
            papers = papers.split(";")
            papers_file = papers_file.split(";")

            for paper, paper_file in zip(papers, papers_file):
                author, article, tail = paper.split('"')
                # paper_file = "../../Publications/Papers/" + paper_file + ".pdf"
                paper_file = paper_file
                script_alumni_people += template.MemberPage.script3_2.format(author, article, tail, paper_file)

        script_alumni_people += template.AlumniPage.script3

        try:
            os.remove("./Alumni/" + name_eng + ".html")
        except OSError:
            pass

        with codecs.open("./Alumni/" + name_eng + ".html", "w", encoding='utf8') as file:
            file.write(script_alumni_people)
            file.close()    
