from attr import attrs
import requests
from bs4 import BeautifulSoup

def filterUrl(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    return soup

def getLinks(soup):
    area = soup.find('div', attrs={'class': 'post-body entry-content'})
    links = area.find_all('a', attrs={'target': '_blank'})
    return links

def getTitle(soup):
    title = soup.find('h3', attrs={'class': 'post-title entry-title'})
    title = title.text
    return title