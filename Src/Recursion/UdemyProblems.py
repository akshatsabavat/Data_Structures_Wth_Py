#Problem -- 1 (Power of Number)
import re


def powerOfNumber(number:int, power:int):
    if power == 0:
        return 1
    elif power == 1:
        return number
    else:
        return number * powerOfNumber(number,power - 1);

print(powerOfNumber(5,10))

def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

