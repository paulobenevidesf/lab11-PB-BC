"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/paulobenevidesf/lab11-PB-BC
# Partner 1: Paulo Jose Benevides Filho
# Partner 2: Benjamin Cao
import math

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a) # log base a of b

def exponent(a, b):
    return a ** b

