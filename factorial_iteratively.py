def factorial_iteratively(n):
    '''
    This function calculates the factorial of a number n iteratively
    Args:
        - n(int): number to calculate factorial
    '''
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial_iteratively(4))
