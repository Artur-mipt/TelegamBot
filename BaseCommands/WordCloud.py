import matplotlib.pyplot as plt
from wordcloud import WordCloud


def word_cloud(bot, update):

    color = update.message.text.split()[1]

    with open('/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/ContentPage', 'r') as file:
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

    path = '/home/artur/PycharmProjects/ParseWikiMipt/NotSrcFiles/cloud.png'
    plt.savefig(path, format='png')
    bot.send_photo(chat_id=update.message.chat_id, photo=open(path, 'rb'))
    plt.clf()
