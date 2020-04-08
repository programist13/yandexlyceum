info = []


def setup_profile(name, vacation_dates):
    global info
    if info == []:
        info.append(name)
        info.append(vacation_dates)
    else:
        info = []
        info.append(name)
        info.append(vacation_dates)


def print_application_for_leave():
    global info
    print(f'Заявление на отпуск в период {info[1]}. {info[0]}')


def print_holiday_money_claim(amount):
    global info
    print(f'Прошу выплатить {amount} отпускных денег. {info[0]}')


def print_attorney_letter(to_whom):
    print(f'На время отпуска в период {info[1]} моим заместителем назначается {to_whom}. {info[0]}')
