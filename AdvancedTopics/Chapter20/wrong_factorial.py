def factorial(N):
    if N <= 1: return 1
    else: return factorial(N-1)

# def factorial(N):
#     print 'N= ', N
#     if N <= 1: retval = 1
#     else: retval = factorial(N-1)
#     print 'retval = ', retval
#     return retval

# def factorial(M, N=1):
#     if M < 2: return N
#     else: return factorial(M-1, M*N)
