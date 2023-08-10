#!/usr/bin/python3
""" Module for obtaining minimum number of operations."""


def minOperations(n):
    """
    minOperations
    Gets fewest number  of operations needed to result in exactly n H characters.Create an array of n + 1 length that will
    hold the minimum no. of operations from 0 characters to `n`
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
