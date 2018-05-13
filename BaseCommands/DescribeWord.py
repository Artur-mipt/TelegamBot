import json
import numpy


def describe_word(bot, update):

    word = update.message.text.split()[1]

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictMain', 'r') as file:
        hist_main = json.load(file)
    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictNext', 'r') as file:
        hist_next = json.load(file)
    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/DictPrev', 'r') as file:
        hist_prev = json.load(file)

    if word not in hist_main:
        not_in_text = 'Данного слова не нашлось в статьях'
        bot.sendMessage(chat_id=update.message.chat_id, text=not_in_text)
        return

    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Слово встречается в тексте {} раз'.format(str(hist_main[word])))

    list_of_frequency = []
    for key in hist_main:
        list_of_frequency.append(hist_main[key])
    average_deviation = numpy.mean(list_of_frequency)

    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Средняя частота по всем словам - {}'.format(average_deviation))
    diff = abs(average_deviation - hist_main[word])
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Отклонение от средней частоты - {}'.format(diff))

    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Слова, встречающиеся после него:')

    for next_word in hist_next[word]:
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='{}'.format(next_word))

    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Слова, встречающиеся перед ним:')

    for prev_word in hist_prev[word]:
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='{}'.format(prev_word))
