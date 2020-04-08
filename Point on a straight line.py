def line(s, t):
    a = s.split('x')
    b = t.split(';')
    a1 = float(a[0])
    a2 = float(a[1])
    b1 = float(b[0])
    b2 = float(b[1])
    n = a1 * b1 + a2
    if n == b2:
        print('True')
    else:
        print('False')
