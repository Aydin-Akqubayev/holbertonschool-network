#!/usr/bin/python3
def add(a, b):

    print(f"{a} + {b} = {a + b}")


def sub(a, b):

    print(f"{a} - {b} = {a - b}")


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """

    print(f"{a} * {b} = {a * b}")


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """

    print(f"{a} / {b} = {int(a / b)}")

add(10, 5)


sub(10, 5)

mul(10, 5)

div(10, 5)
