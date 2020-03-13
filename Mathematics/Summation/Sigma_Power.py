
from Mathematics.Summation.BenGen import B
from Mathematics.Combinatorics.Natural import C
from fractions import Fraction


# TODO expnd to non natural
def sigma_form(n: Fraction):
    """
    Returns the coefficients of Ascending powers of x polynomials that represent the sigma of power n from 1 to x
    :param n: power of each element
    :return: list of coefficients starting with x^1 till x^(n+1)
    """
    return tuple(B(i) * Fraction(C(i + 1, i)) / (n + 1) for i in range(n, -1, -1))
