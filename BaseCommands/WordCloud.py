import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os


def word_cloud(bot, update):

    color = update.message.text.split()[1]

    path = os.getcwd()
    path = path.replace('BaseCommands', '')
    with open('{}/NotSrcFiles/ContentPage'.format(path), 'r') as file:
        text = file.read()

    wordcloud = WordCloud(colormap=color, background_color='white').generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    wordcloud = WordCloud(max_font_size=40,
                          colormap=color,
                          background_color='white').generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

    path = os.getcwd()
    path = path.replace('BaseCommands', '')
    path = '{}/NotSrcFiles/cloud.png'.format(path)
    plt.savefig(path, format='png')
    bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))
    plt.clf()
