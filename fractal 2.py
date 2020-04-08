def defractalize(fractal):
    new_fractal = fractal.copy()
    count = -1
    for i in fractal:
        count += 1
        if new_fractal == i:
            del fractal[count]
            count -= 1
    new_fractal = fractal.copy()
    count = -1
    for i in fractal:
        count += 1
        if new_fractal == i:
            del fractal[count]
            count -= 1
    return fractal
