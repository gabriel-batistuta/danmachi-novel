from modules import folder, link, pdf, chapters, site
from debug import debug

def main():
    debug.clearDiretory()
    folder.makeFolder()
    url = link.getUrl()
    soup = site.filterUrl(url)
    links = site.getLinks(soup)
    title = site.getTitle(soup)
    folder.makeNovelFolder(title)
    pdf.main(links, title)
    pages = chapters.getPages()
    pdf.writeNovel(pages, title)

main()

# translator = Translator()

# pdf = pdfplumber.open('./novel.pdf')

# pages = pdf.pages

# for page in pages:
#     text = page.extract_text()
#     text = text.replace('Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka Kurosaki-Vizard no Fansub', '')
#     text = text.replace('Kurosaki-Vizard no Fansub Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka', '')
#     lista = text.split('\n')
#     for l in lista:
#         trad = translator.translate(l, dest='pt')
#         print(trad.text + '\n')