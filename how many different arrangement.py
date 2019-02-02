def stupid_check(n):
    """
    checking how many different ways are there to arrange 1|2 in n size
    :param n: int
    :return: int
    """

    if n < 0:
        return 0
    if n == 0 or n == 0:
        return 1
    else:
        return stupid_check(n-1) + stupid_check(n-2)


def dp_check(n, mem={}):
    """
    checking how many different ways are there to arrange 1|2 in n size, using memo and DP
    :param n: int
    :param mem: dict
    :return: int
    """

    if mem.get(n, 0):
        return mem[n]
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        mem[n] = dp_check(n-1) + dp_check(n-2)
        return mem[n]



