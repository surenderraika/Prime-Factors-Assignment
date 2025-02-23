"""
Prime Factors Module
This module contains a function to generate prime factors of a given number.
"""

def generate_prime_factors(n):
    """Returns a list of prime factors for the given number n."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n == 1:
        return []    
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
