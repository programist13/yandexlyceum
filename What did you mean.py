numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []  # нечетные
even = []  # четные
for number in numbers:  # цикл по массиву чисел
    if number % 2 == 0:  # если четное
        even.append(number)  # то добавить в массив четных
    else:  # иначе
        odd.append(number)  # нечетных
# в исходном коде массивы были равны друг другу
# здесь эта ошибка исправлена
