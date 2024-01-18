def score(x, y):
    is_in = (x - 0) ** 2 + (y - 0) ** 2
    if is_in <= 1**2:
        return 10
    if is_in <= 5**2:
        return 5
    if is_in <= 10**2:
        return 1

    return 0
