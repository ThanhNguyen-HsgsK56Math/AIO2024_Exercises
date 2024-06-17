import math 
def factorial(n):
    ''' This function compute n! '''
    result = 1
    for i in range(1,n+1):
        result = result*i 
    return result 

def approximate_sin(x, n):
    '''This function approximate sin(x) by Taylor series up to x^n'''
    sin = 0
    for i in range(0,n+1):
        sin = sin + ((-1)**i)*((x**(2*i+1))/factorial(2*i+1)) 
    return sin

def approximate_cos(x, n):
    '''This function approximate cos(x) by Taylor series up to x^n'''
    cos = 0
    for i in range(0,n+1):
        cos = cos + ((-1)**i)*((x**(2*i))/factorial(2*i)) 
    return cos

def approximate_sinh(x, n):
    '''This function approximate sinh(x) by Taylor series up to x^n'''
    sinh = 0
    for i in range(0,n+1):
        sinh = sinh + ((x**(2*i+1))/factorial(2*i+1)) 
    return sinh

def approximate_cosh(x, n):
    '''This function approximate sine(x) by Taylor series up to x^n'''
    cosh = 0
    for i in range(0,n+1):
        cosh = cosh+ ((x**(2*i))/factorial(2*i)) 
    return cosh

x = float(input())
n = int(input())

#Print results
print(f'sin(x) ~ {approximate_sin(x, n)}')
print(f'cos(x) ~ {approximate_cos(x, n)}')
print(f'sinh(x) ~ {approximate_sinh(x, n)}')
print(f'cosh(x) ~ {approximate_cosh(x, n)}')
