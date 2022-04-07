import PyPDF2
import os
import re

for file_name in os.listdir("./informes/"):
    print(file_name)
    load_pdf = open(r'./informes/'+file_name,'rb')
    read_pdf = PyPDF2.PdfFileReader(load_pdf, strict="False")
    page_count= read_pdf.getNumPages()
    alcances_page=read_pdf.getPage(3)
    page_content= alcances_page.extractText()
    alcances_todos = re.search(r'Población(\n.+){13}', page_content).group()
    page_content= alcances_todos.replace('\n','')
    #print(alcances_todos)
    print(page_content)
    print('------------------------------------------------')


# 10 digit Mobile Num Extraction
#alcances_todos = re.search(r'Población(\n.+){10}', page_content).group()
#print(alcances_todos)
