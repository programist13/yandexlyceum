def encrypt_caesar(msg, shift=3):
    letters = 'ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮюбьтимсчяэждлорпавыфъхзщшгнекуцй'
    res = ''
    for i in msg:
        if i in letters:
            if chr(ord(i) + shift) in letters:
                if i == i.lower():
                    res += (chr(ord(i) + shift)).lower()
                else:
                    res += chr(ord(i) + shift)
            elif (ord(i) + shift) > ord('я'):
                count = int(ord(i) + shift - int(ord('я'))) - 1
                if i == i.lower():
                    count = int(ord(i) + shift - int(ord('я'))) - 1
                    res += (chr(ord('а') + count)).lower()
                else:
                    count = int(ord(i) + shift - int(ord('я'))) - 1
                    res += (chr(ord('а') + count))
        else:
            res += i
    return res


def decrypt_caesar(msg, shift=3):
    mes = encrypt_caesar(msg, -shift)
    return mes
