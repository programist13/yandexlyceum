food = {}


def diet(eda):
    global food
    eda = eda.replace(' ', '').split(',')
    for i in eda:
        count_diet = 0
        count_bad = 0
        if i in food['жирное'] or food['сладкое'] or food['мучное']:
            count_bad += 1
        elif i in food['диетическое']:
            count_diet += 1
    if count_bad > count_diet:
        return 'Не ешь столько, По!'
    else:
        return 'Так держать, Воин Дракона!'