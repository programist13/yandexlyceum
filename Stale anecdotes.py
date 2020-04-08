sett = []


def print_only_new(message):
    global sett
    if message not in sett:
        print(message)
        sett.append(message)
    else:
        sett.append(message)



