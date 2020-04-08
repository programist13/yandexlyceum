kvz_result = ''


def polite_input(question):
    a = ''
    podskazka = ''
    global kvz_result
    if kvz_result == '':
        a = input('Как вас зовут?')
        print()
        kvz_result = a
    podskazka = str(kvz_result) + ', ' + question
    input(podskazka)
    print()
    return a

# age = polite_input('укажите возраст')
