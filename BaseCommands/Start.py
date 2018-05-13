def start(bot, update):

    text_start = 'Привет! \n' \
                 'Команды бота - /help \n' \
                 'Введите ссылку на страницу с википедии, глубину поиска\n' \
                 'Пример:\n' \
                 'https://ru.wikipedia.org/wiki/page123 10' \

    bot.sendMessage(chat_id=update.message.chat_id, text=text_start)
