def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    pass


def isPalindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def get_palindrome(min_factor, max_factor, candidates):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for product in candidates:
        if isPalindrome(product):
            result = []
            for i in range(min_factor, max_factor + 1):
                if (product // i) * i == product and (product // i) in list(
                    range(min_factor, max_factor + 1)
                ):
                    result.append([i, product // i])
            if len(result) > 0:
                return product, (x for x in result)
    return None, iter(())


def largest(min_factor, max_factor):
    return get_palindrome(
        min_factor,
        max_factor,
        range(max_factor * max_factor, min_factor * min_factor - 1, -1),
    )


def smallest(min_factor, max_factor):
    return get_palindrome(
        min_factor,
        max_factor,
        range(min_factor * min_factor, max_factor * max_factor + 1),
    )
