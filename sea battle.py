def horizontal(data):
    field1 = [line.split() for line in data.split('\n')]
    res1 = []
    res1.append(field1[3])
    res1.append(field1[2])
    res1.append(field1[1])
    res1.append(field1[0])
    return res1


def vertical(data):
    res2 = []
    field2 = [line.split() for line in data.split('\n')]
    for i in field2:
        for j in i:
            res2.append([j[::-1]])
    return res2


def transposition(data):
    field3 = [line.split() for line in data.split('\n')]
    n1 = (field3[0][0])
    n2 = (field3[1][0])
    n3 = (field3[2][0])
    n4 = (field3[3][0])
    res3 = [[n1[0] + n2[0] + n3[0] + n4[0]], [n1[1] + n2[1]
                                              + n3[1] + n4[1]], [n1[2] + n2[2] + n3[2] + n4[2]],
            [n1[3] + n2[3] + n3[3] + n4[3]]]
    return res3


def main():
    global data
    field = [line.split() for line in data.split('\n')]
    print(field)
    print(horizontal(data))
    print(vertical(data))
    print(transposition(data))
    print(vertical(horizontal(data)))
    print(horizontal(transposition(data)))
    print(vertical(transposition(data)))
    print(transposition(vertical(horizontal(data))))


data = '''1110
0000
1011
1000'''
