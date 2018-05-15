import urllib.request
from bs4 import BeautifulSoup
from ParsingPage.BuildingModel import build_dict_next, build_dict_prev, build_dict_main
import re
import os


def get_html(url):

    response = urllib.request.urlopen(url)
    return response.read()


def parse_html(html, hist_next, hist_prev, hist_main, used_links):

    soup = BeautifulSoup(html, 'html.parser')

    # getting main part of page
    main_part = soup.find('div', class_='mw-parser-output')

    # getting paragraphs in main part
    paragraphs = main_part.find_all('p')

    # getting words from main part
    s = str(paragraphs).lower()
    s = s.replace('>', ' ')
    s = s.replace('<', ' ')
    reg = re.compile('[^а-яА-Я ]')
    s = reg.sub('', s)
    s = re.sub(r'\s+', ' ', s)
    s = s.replace('страница', '')
    s = s.replace('отсутствует', '')

    path = os.getcwd()
    path = path.replace('ParsingPage', '')
    with open('{}/NotSrcFiles/ContentPage'.format(path), 'a') as file:
        file.write(s)

    words = s.split(' ')

    # adding words to histogramm
    build_dict_next(words, hist_next)
    build_dict_prev(words, hist_prev)
    build_dict_main(words, hist_main)

    # getting links
    links = []
    tag_links = soup.find_all('a')
    for tag in tag_links:
        link = str(tag.get('href'))
        if link[0:6] == '/wiki/' and link[-3:] != '/ru' and link not in used_links:
            links.append('https://ru.wikipedia.org{}'.format(link))
            used_links.add('https://ru.wikipedia.org{}'.format(link))

    return links
