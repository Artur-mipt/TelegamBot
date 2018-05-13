from BaseCommands.DescribeWord import describe_word
import json
import numpy
import matplotlib.pyplot as plt


def in_interval(a, b, c):
    return a < c < b


def describe_frequency(bot, update, hist):

    intro = '=====Распределение частот слов====='
    bot.sendMessage(chat_id=update.message.chat_id, text=intro)

    list_of_frequency = []
    for key in hist:
        list_of_frequency.append(hist[key])

    standart_deviation = numpy.std(list_of_frequency)
    average_deviation = numpy.mean(list_of_frequency)

    frequency_hist = {}

    for key in hist:
        frequency = hist[key]
        a = average_deviation - 3 * standart_deviation
        b = average_deviation + 3 * standart_deviation
        if in_interval(a, b, frequency):
            if frequency in frequency_hist:
                frequency_hist[frequency] += 1
            else:
                frequency_hist[frequency] = 1

    x = []
    y = []
    for key in sorted(frequency_hist):
        x.append(key)
        y.append(frequency_hist[key])

    line_frequency = plt.plot(x, y, 'go:')
    plt.axis([0.0, 15.0, 0.0, 150.0])
    plt.xlabel(u'Частота слова')
    plt.ylabel(u'Кол-во слов с такой частотой')
    plt.grid()

    path = '/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/frequency.png'
    plt.savefig(path, format='png')
    bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))
    plt.clf()


def describe_length(bot, update, hist):

    intro = '=====Распределение длин слов====='
    bot.sendMessage(chat_id=update.message.chat_id, text=intro)

    length_hist = {}

    for key in hist:
        length = len(key)
        if length in length_hist:
            length_hist[length] += hist[key]
        else:
            length_hist[length] = hist[key]

    x = []
    y = []
    for key in sorted(length_hist):
        x.append(key)
        y.append(length_hist[key])

    line_length = plt.plot(x, y, 'r^:')
    plt.axis([0.0, 20.0, 0.0, 200.0])
    plt.xlabel(u'Длина слова')
    plt.ylabel(u'Кол-во слов с такой длиной')
    plt.grid()

    path = '/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/length.png'
    plt.savefig(path, format='png')
    bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))
    plt.clf()


def describe(bot, update):

    if update.message.text != '/describe':
        describe_word(bot, update)
        return

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictMain', 'r') as file:
        hist = json.load(file)

    describe_frequency(bot, update, hist)
    describe_length(bot, update, hist)
