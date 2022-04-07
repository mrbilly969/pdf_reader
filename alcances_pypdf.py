# Extracción de datos x informe
# Autor: Andrés Ortega Martínez (xerxes)
# Extrae cifras de población de I. de Resultados (IR)
import PyPDF2
import os
import re

#Apunta a un repositorio de informes
for file_name in os.listdir("./informes/"):
    print(file_name)
    load_pdf = open(r'./informes/'+file_name,'rb')
    read_pdf = PyPDF2.PdfFileReader(load_pdf, strict="False")
    page_count= read_pdf.getNumPages()

    # Apunta a la página 4 del IR, esta tiene la información de interés.
    alcances_page=read_pdf.getPage(3)
    page_content= alcances_page.extractText()

    # De la página seleccionada, con expresiones regulares, se solicitan los datos
    alcances_todos = re.search(r'Población(\n.+){13}', page_content).group()
    page_content= alcances_todos.replace('\n','')
    print(page_content)
    print('------------------------------------------------')
