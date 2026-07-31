import math


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    
    # Handle edge cases
    if n <= 1:
        return False
    
    # Check divisibility up to sqrt of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            
    return True


def find_primes(limit: int) -> list:
    """Find all prime numbers up to a given limit."""
    primes = []
    
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
            
    return primes
