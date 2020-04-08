lastTicket = 0


def lucky(ticket):
    global lastTicket
    a = str(lastTicket)
    lastTicket = '000000' + str(lastTicket)
    lastTicket = lastTicket[::-1]
    a = str(lastTicket)
    n1 = int(a[0]) + int(a[1]) + int(a[2])
    n2 = int(a[3]) + int(a[4]) + int(a[5])
    ticket = '000000' + str(ticket)
    ticket = ticket[::-1]
    a1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    a2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if n1 == n2 and a1 == a2:
        return 'Счастливый'
    else:
        return 'Несчастливый'
