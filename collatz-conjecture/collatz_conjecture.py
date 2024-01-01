def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    n = number
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        step += 1
    return step
