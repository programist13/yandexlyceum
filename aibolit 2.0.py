def hello(name):
    count = 0
    global query
    if None not in query:
        print(f'Простите, {name}. Все окна заняты')
    for i in query:
        count += 1
        if i is None:
            print(f'Здравствуйте, {name}! Подойдите к окошку номер {count}')
            query[count - 1] = name
            count = 0
            break


def search_card(name):
    global query
    global base
    count = -1
    if name in query:
        for i in base:
            count += 1
            if i == name:
                print(f'Ваша карта с номером {count + 1} найдена')
                break
    if name not in query:
        print(f'Простите, {name}, дождитесь своей очереди')
    if name not in base and name in query:
        print(f'Ваша карта не найдена')


def good_bye(name):
    global query
    if name in query:
        print(f'До свидания, не болейте, {name}')
        query.remove(name)
        query.append(None)
    else:
        print(f'Простите, {name}, дождитесь своей очереди')
