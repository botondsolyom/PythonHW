# Calculation logic

def calc_pow(base: float, exponent: float) -> float:
    return base ** exponent


def calc_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative number")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calc_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative number")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
