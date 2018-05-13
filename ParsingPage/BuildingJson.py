from ParsingPage.ParseHtml import get_html, parse_html
import json
import os


def build_json(bot, update):

    path = '/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/ContentPage'
    with open(path, 'w'):
        pass

    url = update.message.text.split()[0]
    depth = update.message.text.split()[1]

    hist_next = {}
    hist_prev = {}
    hist_main = {}
    links = [url]
    used_links = set(url)

    for i in range(0, int(depth), 1):
        new_links = []
        for link in links:
            html = get_html(link)
            parse_result = parse_html(html, hist_next, hist_prev, hist_main, used_links)
            new_links.extend(parse_result)
        links = new_links

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictNext', 'w') as file:
        json.dump(hist_next, file)

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictPrev', 'w') as file:
        json.dump(hist_prev, file)

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictMain', 'w') as file:
        json.dump(hist_main, file)
