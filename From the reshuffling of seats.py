# есть разница
value = [1, 2, 3]
addition = value  # теперь изменяя один массив изменяется и другой
value += [4, 5, 6]
print(addition)
value1 = [1, 2, 3]
addition1 = value1
value1 = value1 + [4, 5, 6]  # а в этом случае изменяется конкретный массив, не изменяя другой
print(addition1)
# нет разницы: идет сложение чисел, поэтому результат не меняется
one = 1
two = 2
one += two
print(one)
one1 = 1
two1 = 2
one1 = one1 + two1
print(one1)
