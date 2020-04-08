def matrix(n=0, m=0, a=''):
    if n == 0:
        x = []
        x.append([0])
        return x
    elif n > 0 and m == 0 and a == '':
        x = []
        for i in range(n):
            x.append([])
        for i in range(n):
            for j in range(n):
                x[i].append(0)
        return x
    elif n > 0 and m > 0 and a == '':
        x = []
        for i in range(n):
            x.append([])
        for i in range(n):
            for j in range(m):
                x[i].append(0)
        return x
    elif n > 0 and m > 0 and a != '':
        x = []
        for i in range(n):
            x.append([])
        for i in range(n):
            for j in range(m):
                x[i].append(a)
        return x
