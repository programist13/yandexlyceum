def eratosthenes(N):
    numbers = []
    p_numbers = []
    s_numbers = []
    for i in range(2, N + 1):
        numbers.append(i)
    for j in numbers:
        for i in numbers:
            n = j
            if i % n == 0 and i > n:
                s_numbers.append(i)
                numbers.remove(i)
    print(*s_numbers)



