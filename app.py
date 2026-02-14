def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


import math


def square_root(a: int) -> float:
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)
