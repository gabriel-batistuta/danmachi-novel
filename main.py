# from modules import folder, link, pdf, chapters, site
# from debug import debug
from googletrans import Translator
from os import listdir

URL_COM = 'translate.google.com'
URL_LV = 'translate.google.lv'
LANG = "pt"

translator = Translator(service_urls=[URL_COM, URL_LV])
# translation = translator.translate(text, dest=lang)

if __name__ == '__main__':
    for file in listdir('./'):
        if '.pdf' in file:
            # translate_pdf(file, LANG)
            print('concluido')

            