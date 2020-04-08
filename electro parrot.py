phrases = []


def parrot(phrase):
    global phrases
    if phrase in phrases:
        print(phrase)
        phrases.append(phrase)
    else:
        phrases.append(phrase)

# parrot("Привет!")
# parrot("Привет!")
# parrot("Как дела?")
# parrot("Привет")
# parrot("Как тебя зовут?")
# parrot("Привет")
