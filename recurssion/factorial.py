def factorial(n):
    return 1 if n in [0, 1] else n * factorial(n - 1)


print(factorial(6))
