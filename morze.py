# зададим таблицу кодов
MorseCode = {'A': '.−', 'B': '−...', 'C': '−.−.', 'D': '−..', 'E': '.',
             'F': '..−.', 'G': '−−.', 'H': '....', 'I': '..',
             'J': '.−−−', 'K': '−.−', 'L': '.−..', 'M': '−−', 'N': '−.',
             'O': '−−−', 'P': '.−−.', 'Q': '−−.−',
             'R': '.−.',
             'S': '...', 'T': '−', 'U': '..−', 'V': '...−', 'W': '.−−',
             'X': '−..−', 'Y': '−.−−', 'Z': '−−..'}


def encode_to_morse(text):
    t = ''
    global MorseCode
    for i in text.upper():
        t += MorseCode[i]
        t += ' '
    return t


def decode_from_morse(code):
    global MorseCode
    mes = ''
    code = code.split()
    for i in code:
        for k, v in MorseCode.items():
            if i == v:
                mes += k
    return mes


def main():
    a = ''
    cikle = True
    while cikle:
        a = int(input(
            'Ввведите счисло для выбора действия: 1 кодировать, 2 декодировать, 0 выход '))
        print()
        if a == 1:
            print(encode_to_morse(input('введите текст для кодирования')))
        if a == 2:
            print(decode_from_morse(input('введите текст для декодирования')))
        if a == 0:
            cikle = False


main()
