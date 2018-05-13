def build_dict_next(words, hist):

    for i in range(0, len(words) - 1, 1):
        current = words[i]
        next = words[i + 1]
        if current == '' or current == 'страница' or current == 'отсутствует'\
                or next == '' or next == 'страница' or next == 'отсутствует':
            continue

        if current in hist:
            if next in hist[current]:
                hist[current][next] += 1
            else:
                hist[current][next] = 1
        else:
            hist[current] = {}
            hist[current][next] = 1


def build_dict_prev(words, hist):

    for i in range(0, len(words) - 1, 1):
        current = words[i]
        next = words[i + 1]
        if current == '' or current == 'страница' or current == 'отсутствует'\
                or next == '' or next == 'страница' or next == 'отсутствует':
            continue

        if next in hist:
            if current in hist[next]:
                hist[next][current] += 1
            else:
                hist[next][current] = 1
        else:
            hist[next] = {}
            hist[next][current] = 1


def build_dict_main(words, hist):

    for i in range(0, len(words), 1):
        current = words[i]
        if current == '' or current == 'страница' or current == 'отсутствует':
            continue
        if current in hist:
            hist[current] += 1
        else:
            hist[current] = 1
