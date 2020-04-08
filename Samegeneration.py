def samegeneration(email='', name='', place='Ханты-Мансийске', date=''):
    if place == '':
        return f'To: {email} Здравствуйте, {name}! Были бы рады видеть вас' \
               f' на встрече начинающих программистов в {place}, которая пройдет {date}.'
    else:
        return f'To: {email} Здравствуйте, {name}! Были бы рады видеть вас ' \
               f'на встрече начинающих программистов в {place}, которая пройдет {date}.'


print(samegeneration(email='privet@mail.ru', name='Николай', place='Москве', date='01-01-2021'))
print(samegeneration(email='privet@mail.ru', name='Николай', date='01-01-2021'))
