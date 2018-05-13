import json
import numpy


def in_interval(a, b, c):
    return a < c < b


def stop_words(bot, update):

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictMain', 'r') as file:
        hist = json.load(file)

    intro = '=====Слова-выбросы====='
    bot.sendMessage(chat_id=update.message.chat_id, text=intro)

    list_of_frequency = []
    for key in hist:
        list_of_frequency.append(hist[key])

    standart_deviation = numpy.std(list_of_frequency)
    average_deviation = numpy.mean(list_of_frequency)
    a = average_deviation - 3 * standart_deviation
    b = average_deviation + 3 * standart_deviation

    for key in hist:
        frequency = hist[key]
        if not in_interval(a, b, frequency):
            bot.sendMessage(chat_id=update.message.chat_id,
                            text='{}'.format(key))
