from copy import copy


def mirror(arr):
    arr_reverse = copy(arr)  # копируем данный список
    arr_reverse.reverse()  # "разворачиваем" скопированный список
    arr.extend(arr_reverse)  # к данному списку прибавляем развернутый
