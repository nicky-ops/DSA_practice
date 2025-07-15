def factorial(n):
    """
    This function calculates the factorial of a number using the recursive strategy
    Args:
        - n(int): input to calculate factorial
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



print(factorial(4))

