#!/usr/bin/python3
"""
RSA Factoring Challenge
"""


from sys import argv
import random


def gcd(a, b):
    """
    A function that returns the greatest common divisor

    Argumnets:
        a: first number
        b:second number

    Return:
        return the geatest common divisor
    """

    while b:
        a, b = b, a % b
    return a


def pollard_rho(n):
    """
    Pollard's Rho algorithm that factorise semi-prime numbers

    Arguments:
        n: input value

    Return:
        prime factor
    """

    def f(x):
        """
        Utility function

        Return:
            (x * x + 1) % n
        """

        return (x * x + 1) % n

    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d


def factorize(n):
    """
    Factorize function

    Return:
        n = p*q
    """

    factors = []
    number = n
    divisor = 2

    if n <= 1:
        return

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            factor = pollard_rho(n)
            factors.append(factor)
            n //= factor

    if len(factors) > 1:
        p, q = factors[0], 1
        for i in range(1, len(factors)):
            q *= factors[i]
        print(f"{number}={q}*{p}")
    else:
        print("Number is prime")


def main():
    """
    Entry point of the program, it opens a file calls factorize function
    to return the smallest prime number making up the product
    """

    if len(argv) < 2:
        print("Usage: factors <file>")
        return

    try:
        with open(argv[1], 'r') as file:
            for lines in file:
                line = lines
                if len(line) > 18:
                    continue
                factorize(int(line))
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")


if __name__ == "__main__":
    main()
