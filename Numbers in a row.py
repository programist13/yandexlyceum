def from_string_to_list(string, container):
    num = []
    string = string.split()
    for i in string:
        num.append(int(i))
    container.extend(num)
    return container
