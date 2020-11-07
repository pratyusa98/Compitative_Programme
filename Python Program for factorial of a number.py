"""
 factorial of 6 is 6*5*4*3*2*1 which is 720
By Recursive :
"""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        n * factorial(n-1)