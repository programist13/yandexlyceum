a = sum(map(lambda x: x ** 2, filter(lambda x: len(str(x)) == 2 and x % 9 == 0, range(10, 100))))
print(a)
# 40905
