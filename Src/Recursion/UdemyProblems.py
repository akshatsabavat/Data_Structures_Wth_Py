from array import *
from ast import Num
import re

#Problem -- 1 (Power of Number)
def powerOfNumber(number:int, power:int):
    if power == 0:
        return 1
    elif power == 1:
        return number
    else:
        return number * powerOfNumber(number,power - 1);

print(powerOfNumber(5,10))

#Problem -- 2 (Factorial)
def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

#Problem -- 3 (Product of an array)
arrayProduct = array('i',[1,2,3,10])

def productOfArray(arr):
    product = 1 #Looping variable
    for i in arr:
        product = product * i
    return product

print(productOfArray(arrayProduct))

#Problem -- 4 (Recursive Range adds numbers from 0 till the number in the parameter)

def recursiveRange(n):
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n-1)

print(recursiveRange(6))

#Problem -- 5 (Fibonnaci)
def fibonnaci(n):
    if n in [0,1]:
        return n
    else:
        return fibonnaci(n-2) + fibonnaci(n-1)

print(fibonnaci(10))

#Problem -- 6 (Reverse a string)
word = 'Akshat'
def reverseString(string):
