# def factorial(n):
#     if (n < 0):
#         raise 'NegativeNumberError'
#     elif (n == 0) or (n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

def factorial(m, n=1):
    if (m < 0):
        raise 'NegativeNumberError'
    elif (m < 2):
        return n
    else:
        return factorial(m-1, m*n)
