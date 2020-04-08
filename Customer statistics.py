transactions = []
new_transactions = {}
action = []
new_action = []


def get_transactions(t):
    global transactions, new_transactions
    if t == 'print_it':
        for i in transactions:
            n = int(i[1])
            d = i[0]
            new_transactions[d] += n
        for i in new_action:
            a = action.count(i)
            print(f'{a} {i} {new_transactions[i]}')
    else:
        t = t.split('-')
        t = (t[1].split(':'))
        transactions.append(t)
        action.append(t[0])
        if t[0] not in new_action:
            new_action.append(t[0])
        if t[0] not in new_transactions:
            new_transactions[t[0]] = 0
