def date_analysis(dates):
    minn = ''
    mes = ''
    res = ''
    for i in dates:
        if (int(i[3:5]) == 12) or (int(i[3:5]) == 1) or (int(i[3:5]) == 2):
            if i[3:5] == '12':
                mes = '00'
            else:
                mes = i[3:5]
            if (minn == '') or (minn > (mes + str(i[0]) + str(i[1]))):
                minn = mes + str(i[:2])
                res = i
    return res



