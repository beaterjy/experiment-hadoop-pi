from mpmath import inf, mp, nsum


def pi_compute(n):
    """
    >>> pi_compute(50)
    '3.1415926535897932384626433832795028841971693993751'
    """
    mp.dps = n  # accuracy
    return str(nsum(lambda k: (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) / 16**k, (0, inf)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

