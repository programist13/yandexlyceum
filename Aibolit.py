base = []


def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...', sep='/n')


def search_card(name):
    global base
    count = -1
    for i in base:
        count += 1
        if i == name:
            print(f'Ваша карта с номером {count + 1} найдена', sep='/n')
            break
    if name not in base:
        print(f'Ваша карта не найдена')

