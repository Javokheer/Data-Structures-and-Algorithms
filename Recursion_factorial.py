def fact(n):
    """
    Returns n factorial

    Input: n positive integer

    Output: nth factorial

    >>> fact(4)
    24
    """
    return n * fact(n - 1) if n >= 1 else 1


