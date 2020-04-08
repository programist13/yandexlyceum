check_counter = 0
items = []


def add_item(item_name, item_cost):
    global items
    items.append([item_name, item_cost])


def print_receipt():
    global items
    if items != []:
        global check_counter
        check_counter += 1
        print('Чек ' + str(check_counter) + '. Всего предметов: ' + str(len(items)))
        total = 0
        for i in items:
            total += int(i[1])
            print(i[0], '-', i[1])
        print('Итого:', total)
        print('-----')
        items = []
