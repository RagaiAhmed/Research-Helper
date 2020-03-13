"""
    Bernoulli Number Generator script

    After messing around with bernoulli numbers it can be proved that :
        B(i) = (  i - sigma( 1, i-1, lambda r : C(i+1, r) * B(r) )  ) / (i+1)

    So this script uses such method to generate bernoulli numbers where i>1
"""
from fractions import Fraction
from Mathematics.Summation.Sigma import sigma
from Mathematics.Combinatorics.Natural import C

# For memoization with B(0) = 1 , B(1) = 1/2
BERNOULLI = {0: Fraction(1), 1: Fraction(1, 2)}


def B(i: Fraction):
    # If stored before
    if i in BERNOULLI:
        return BERNOULLI[i]

    s = sigma(1, i - 1, lambda r: (Fraction(C(i + 1, r)) * B(r)))
    res = (i - s) / (i + 1)
    BERNOULLI[i] = res
    return res
