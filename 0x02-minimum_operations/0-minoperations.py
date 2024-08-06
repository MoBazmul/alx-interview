#!/usr/bin/python3

def minOperations(n):
    """
    Compute the minimum number of operations to get exactly n 'H' characters
    using 'Copy All' and 'Paste'.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: Minimum number of operations required. Returns 0 if n <= 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

