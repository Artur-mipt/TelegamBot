def help(bot, update):

    text_top = 'Получить топ N наиболее часто(редко) встречающихся слов:\n' \
               '/top N frequent (/top N rare) \n\n'

    text_stop_words = 'Получить слова-выбросы:\n' \
                      '/stop_words \n\n'

    text_cloud = 'Получить облако слов в указанной цветовой гамме:\n' \
                 '/word_cloud COLOR \n\n'

    text_describe = 'Получить распределение частот и длин слов:\n' \
                    '/describe \n\n'

    text_describe_word = 'Получить всю доступную статистику по конкретному слову:\n' \
                         '/describe WORD \n\n'

    bot.sendMessage(chat_id=update.message.chat_id,
                    text='{}{}{}{}{}'.format(text_top,
                                             text_stop_words,
                                             text_cloud,
                                             text_describe,
                                             text_describe_word))
