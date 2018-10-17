import math
import hypothesis.strategies as st
from hypothesis import given, settings


# Checks whether a number is definitely prime
def is_prime(n):
    # 2 and 3 are prime numbers
    if n == 2 or n == 3:
        return True
    # Filter multiples of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Ignore negative numbers and large numbers
    if n < 2 or n > 10000:
        return False
    r = int(n ** 0.5)
    # Prime numbers greater than 4 can only be of the form 6n - 1 or 6n + 2
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


# Checks whether a number is probably prime
def is_probably_prime(n):
    # Ignore negative numbers and large numbers
    if n < 2 or n > 10000:
        return False
    # Check all congruence classes of a that could be coprime to n
    for a in range(n):
        if math.gcd(n, a) == 1 and pow(a, n - 1, n) != 1:
            return False
    return True


Values = st.integers()


@settings(max_examples=10000)
@given(Values)
def test_carmichael(v):
    # By Fermat's little theorem, a^(n - 1) = 1 mod n for all a with (a, n) = 1
    # The only exceptions to this rule are Carmichael numbers which are rare
    # Below 10000 only 561, 1105, 1729, 2465, 2821, 6601, 8911 are Carmichael
    assert is_prime(v) == is_probably_prime(v), "Catch a Carmichael number " + str(v)


"""
Refreshing the cache will force pytest to randomly choose numbers,
so a Carmichael number will not always be found in the first few runs,
and as such the test should initially return Pass for small max_examples.
Once a Carmichael number is found, the test would return Failure,
but subsequently pytest will remember the number found and fail immediately.
"""