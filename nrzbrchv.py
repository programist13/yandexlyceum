translated_text = None
text2 = ' '


def translate(text):
    z = ' чсмтьбждлрпвфйцкнгшщзхъЧСМТЬБЖДЛРПВФЙЦКНГШЩЗХЪ'
    global translated_text
    global text2
    for i in text:
        if i != text2:
            if i not in z:
                text = text.replace(i, '')
                text2 = i
    translated_text = ' '.join(text.split())
    return translated_text
