"""
    Implementation of combinatorics popular notations in natural numbers
"""

# For memoization with 0! = 1 , 1! = 1
FACTORIALS = {0: 1, 1: 1}

#TODO EXPAND TO NON NATURAL

# TODO add decorators for checking input ranges
def C(n, r):
    """
        Implements combinations where n and r are natural numbers and n>=r
        Where it finds the number of ways you could make r sized subsets from a set of n elements
    :param n: number of elements
    :param r: number of places (positions)
    :return: number of ways you could put these distinct elements in these positions where order doesn't matter
    """
    # Check for possible optimization
    if r > n / 2:
        r = n - r

    # Compute permutations and eliminate order
    return P(n, r) / fact(r)


# TODO add decorators for checking input ranges
def P(n, r):
    """
        Implements permutations where n and r are natural numbers and n >= r
        Where it finds the number of ways you could put r distinct ordered elements from n list of elements
    :param n: number of elements
    :param r: number of places (positions)
    :return: the number of ways you could put these distinct elements in these positions where order matters
    """

    # If factorial values previously stored
    if n in FACTORIALS:
        return FACTORIALS[n] / FACTORIALS[n - r]

    res = 1

    # If a nearer value exists then start from there
    if len(FACTORIALS) - 1 >= n - r + 1:
        res = FACTORIALS[len(FACTORIALS) - 1] / FACTORIALS[n - r]
        r = len(FACTORIALS) - 1
    else:
        r = n - r + 1
    # Compute the rest
    while r <= n:
        res *= r
        r += 1

    return res


# TODO add decorators for input checking
def fact(n):
    """
        Implements factorial for natural numbers
    """
    # If computed before
    if n in FACTORIALS:
        return FACTORIALS[n]
    else:
        # Compute recursively
        res = fact(n - 1) * n
        FACTORIALS[n] = res
        return res
