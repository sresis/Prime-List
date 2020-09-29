"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""
    primes_list = []
    if count == 0:
        return []
    
    i = 2
    while len(primes_list) < count:
 
        if i == 2:
            primes_list.append(2)
        # see if it is divisible by any of the primes so far
        else:
            divis_count = 0
            for num in primes_list:
                if i % num == 0:
                    divis_count += 1
            if divis_count == 0:
                primes_list.append(i)
        i += 1
    return primes_list



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
