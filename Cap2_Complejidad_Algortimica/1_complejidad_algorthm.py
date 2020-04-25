import time
import sys
sys.setrecursionlimit(20000)
def factorial(n):
    '''Factorial, implementacion Iterativa.'''

    respuesta = 1

    while n > 1:
        respuesta *= n  # v. actual * n, n-1, n-2, etc
        n -= 1

    return respuesta

def factorial_r(n):
    '''Factorial, implementacion Recursiva.'''
    if n == 1:  # Caso Base
        return 1

    else:
        return n * factorial_r(n - 1)  # Regresa n* n-1

if __name__ == '__main__':
    n = 2000

    comienzo = time.time()
    # print(factorial(n))
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    # print(factorial(n))
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
