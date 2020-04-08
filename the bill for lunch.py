daily_food = []


def count_food(days):
    global daily_food
    total = 0
    for i in days:
        total += daily_food[i - 1]
    return total

# daily_food = [0, 150, 150]
# print(count_food([1]))
# daily_food = [0, 150, 150]
# print(count_food([2, 3]))
