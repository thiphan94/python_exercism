def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    factors = range(min_factor, max_factor + 1)
    products = range(max_factor**2, (min_factor**2) - 1, -1)

    return list_palindrome(factors, products)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    factors = range(min_factor, max_factor + 1)
    products = range(max_factor**2, (min_factor**2) - 1, -1)

    products = range(min_factor**2, (max_factor**2) + 1)
    return list_palindrome(factors, products)


def list_palindrome(factors, products):
    results = []
    for number in products:
        if str(number) == str(number)[::-1]:
            for factor in factors:
                divisor, remainder = divmod(number, factor)
                if remainder == 0 and divisor in factors:
                    results.append([factor, divisor])
        if results:
            return number, results
    return None, []
