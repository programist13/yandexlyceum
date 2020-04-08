def number_in_english(number):
    s = ''
    num1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'one', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen', }
    num3 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety'}
    res = []
    # если есть сотни в числе
    if number == 0:
        print('zero')
    if len(str(number)) == 3:
        res.append(num1[int(str(number)[0])])
        res.append(' hundred')
        # проверим что количество сотен не ровное
        if 0 < number % 100:
            res.append(' and ')
    number = number % 100
    if len(str(number)) == 2:
        if number > 19:
            jj = str(number)[0]
            ii = int(jj)
            z = num3[ii * 10]
            res.append(z)

            number = number % 10
            if number > 0:
                res.append(' ')
                res.append(num1[number])
        elif number > 0:
            res.append(num1[number])
    elif len(str(number)) == 1 and number > 0:
        res.append(num1[number])
    for i in res:
        s += i

    return s
