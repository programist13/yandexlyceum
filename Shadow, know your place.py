def make_shades(alley, k):
    alley2 = alley
    if k < 0:
        alley = reversed(alley)

    count = 0
    res = []
    if k == 0:
        for i in alley:
            if i > 0:
                res.append(True)
            else:
                res.append(False)
    else:
        count = -1
        for i in alley:
            if i > 0 and count > 0 and (i > count):
                count = (i - count) * k
                for i in range(count * k + 1):
                    res.append(True)
            elif count > 0:
                count -= 1
            else:
                if i > 0:
                    count = -1
                    for j in range(i * abs(k) + 1):
                        count += 1
                        res.append(True)
                else:
                    res.append(False)

    res2 = []
    for i in range(len(alley2)):
        res2.append(res[i])
    if k < 0:
        res2 = reversed(res2)
    res = []
    for i in res2:
        res.append(i)
    return res


def calculate_sunny_length(shades):
    count = 0
    for i in shades:
        if not i:
            count += 1
    return count


def main():
    a = int(input())
    b = input().split()
    c = []
    for i in b:
        c.append(int(i))
    d = make_shades(c, a)
    counter = calculate_sunny_length(d)
    if counter >= 10:
        print('Обгорел')
    else:
        print('Тени достаточно')
