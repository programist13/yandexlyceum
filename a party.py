friends = []


def add_friends(name_of_person, list_of_friends):
    global friends
    friends.append([name_of_person, list_of_friends])


def are_friends(name_of_person1, name_of_person2):
    global friends
    a = False
    for i in friends:
        for j in i[1]:
            if ((name_of_person1 == i[0]) and (name_of_person2 in j)) or (
                    (name_of_person2 == i[0]) and (name_of_person1 in j)):
                a = True
    return a


def print_friends(name_of_person):
    frlist = []
    global friends
    for i in friends:
        for j in i[1]:
            if name_of_person == i[0]:
                frlist.append(j)
    for i in friends:
        for j in i[1]:
            if name_of_person == j:
                frlist.append(i[0])
    frlist.sort()
    print(*frlist)
add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
print_friends('Мария')
