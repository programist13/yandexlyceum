one = 0
two = 0
three = 0
numbers = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
           [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
           [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]


def transformation(number):
    res = ''
    if number <= 0:
        return ''
    for arabskie, roman in numbers:
        while number >= arabskie:
            res += roman
            number -= arabskie
    return res


def roman():
    global one, two, three
    three = one + two
    res = f'{transformation(one)} + {transformation(two)} = {transformation(one + two)}'
    print(res)
