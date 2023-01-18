import pdfplumber
import os
from googletrans import Translator

translator = Translator()

pdf = pdfplumber.open('./novel.pdf')

page = pdf.pages[3]

text = page.extract_text()

lista = text.split('\n')

for l in lista:
    trad = translator.translate(l, dest='pt')
    print(trad.text + '\n')