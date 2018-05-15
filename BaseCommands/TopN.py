import json
from operator import itemgetter
import numpy
import os


def in_interval(a, b, c):
    return a < c < b


def top_n(bot, update):

    path = os.getcwd()
    path = path.replace('BaseCommands', '')
    with open('{}/NotSrcFiles/DictMain'.format(path), 'r') as file:
        hist = json.load(file)

    count = int(update.message.text.split()[1])
    frequency = update.message.text.split()[2]

    sorted_list = sorted(hist.items(), key=itemgetter(1))

    list_of_frequency = []
    for key in hist:
        list_of_frequency.append(hist[key])

    standart_deviation = numpy.std(list_of_frequency)
    average_deviation = numpy.mean(list_of_frequency)
    a = average_deviation - 3 * standart_deviation
    b = average_deviation + 3 * standart_deviation

    current_count = 0

    if frequency == 'frequent':
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='Топ {} самых частых слов:'.format(count))
        for i in range(len(sorted_list) - 1, -1, -1):
            pair = sorted_list[i]
            if in_interval(a, b, pair[1]) and current_count < count:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text=pair[0])
                current_count += 1

    if frequency == 'rare':
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='Топ {} самых редких слов:'.format(count))
        for i in range(0, len(sorted_list), 1):
            pair = sorted_list[i]
            if in_interval(a, b, pair[1]) and current_count < count:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text=pair[0])
                current_count += 1
