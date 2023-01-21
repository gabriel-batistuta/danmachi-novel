import pdfplumber
from googletrans import Translator

def getPages():
    translator = Translator()

    pdf = pdfplumber.open('./novel.pdf')

    pages = pdf.pages

    return pages