def tic_tac_toe(field):
    i = field[0]
    j = field[1]
    k = field[2]
    if i[0] == i[1] == i[2] and i[0] != '-':
        print(i[0], 'win')
    elif j[0] == j[1] == j[2] and j[0] != '-':
        print(j[0], 'win')
    elif k[0] == k[1] == k[2] and k[0] != '-':
        print(k[0], 'win')
    elif i[0] == j[0] == k[0] and i[0] != '-':
        print(j[0], 'win')
    elif i[0] == j[1] == k[2] and i[0] != '-':
        print(i[0], 'win')
    elif i[1] == j[1] == k[1] and i[1] != '-':
        print(j[1], 'win')
    elif i[2] == j[2] == k[2] and i[2] != '-':
        print(i[2], 'win')
    elif i[2] == j[1] == k[0] and i[2] != '-':
        print(k[0], 'win')
    else:
        print('draw')
