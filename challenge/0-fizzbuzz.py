#!/usr/bin/python3
"""
FizzBuzz module
"""
import sys


def fizzbuzz(n):
    """
    1-dən n-ə qədər ədədləri FizzBuzz qaydalarına uyğun çap edir
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            tmp_result.append("FizzBuzz")
        elif i % 3 == 0:
            tmp_result.append("Fizz")
        elif i % 5 == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))

    print(" ".join(tmp_result))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        fizzbuzz(100)
    else:
        fizzbuzz(int(sys.argv[1]))
