from calculator import add, subtract, multiply, divide


def add(a, b):
    return a + b


def test_additional():
    assert add(2, 3) == 5


def test_addition_with_neagtive_numbers():
    assert add(-2, 3) == 1


def multiply(a, b):
    return a * b


def test_multiplication():
    assert multiply(2, 3) == 6


def subtract(a, b):
    return a - b


def test_subtraction():
    assert subtract(5, 3) == 2


def test_subtraction():
    assert subtract(6, 5) == 1


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_division():
    assert divide(6, 3) == 2
