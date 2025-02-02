"""
Function Utils for checking numbers
"""
import math
import requests
from django.conf import settings

def is_num_perfect(number: int) -> bool:
    """Check if a number is perfect."""
    return sum(num for num in range(1, number // 2 + 1) if number % num == 0) == number

def is_num_prime(number: int) -> bool:
    """Check if a number is a prime number."""
    if number < 2:  # 0, 1, and negative numbers are not prime
        return False
    for numb in range(2, int(math.sqrt(number)) + 1):
        if number % numb == 0:
            return False
    return True

def return_num_properties(numb: int) -> list:
    """Return properties of a given number (Armstrong, even, odd)."""
    prop = []

    # Armstrong number check
    num_str = str(numb)
    n = len(num_str)
    total = sum(int(digit) ** n for digit in num_str)  # Sum of digits raised to nth power

    if total == numb:
        prop.append("armstrong")

    # Even or Odd check
    prop.append("even" if numb % 2 == 0 else "odd")

    return prop

def sum_number_digit(numb: int) -> int:
    """Sum all the digits of a number."""
    return sum(int(digit) for digit in str(numb))


def get_funfact_for_number(numb: int):
    """Retrieves the fun fact of a number"""
    url = f"{settings.NUMBAPI}/{numb}/math"
    try:
        res = requests.get(url, timeout=5)  # Set timeout to avoid long waits
        res.raise_for_status()  # Raise exception if status code is 4xx/5xx
        return res.text
    except (requests.ConnectionError, requests.Timeout):
        return "No internet connection, unable to fetch fun fact."
    except requests.RequestException:
        return "Failed to retrieve fun fact."