import requests
from bs4 import BeautifulSoup
import urllib.request

def obj(link):
    class Link:
        def __init__(self, link):
            self.title = link.text
            self.link = link['href']
            
    return Link(link)

def main(links, capTitle):
    file = open(f'./novels/{capTitle}/sumary.txt','a+')
    for link in links:
        cap = obj(link)
        file.write(f'{cap.title}\n\n')
        # writeSumary(cap.title, capTitle)
    file.close()

def writeNovel(pages, title):
    import pdfplumber
    from googletrans import Translator
    translator = Translator()

    file = open(f'./novels/{title}/novel.txt','a+')

    for page in pages:
        text = page.extract_text()
        lista = text.split('\n')
        for l in lista:
            trad = translator.translate(l, dest='pt')
            file.write(trad.text + '\n')

    file.close()