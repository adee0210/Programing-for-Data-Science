import math
def solve_factorial(n):
    if n==0:
        return 1
    else:
        return n*solve_factorial(n-1)
    
    
def cos_taylor(x):
    result = 0
    i = 0
    number_next = 1
    while abs(number_next) > 10e-12:
        number_next = (((-1)**i)* x**(2*i))/(solve_factorial(i*2))
        result+=number_next
        i+=1
    
    return result

def sin_taylor(x):
    result = 0
    i = 0
    number_next = 1
    while abs(number_next) > 10e-12:
        number_next = ( ((-1)**i) * x**(2*i+1) )/(solve_factorial(i*2+1))
        result+=number_next
        i+=1
    
    return result
        


x = eval(input())


print(f'Gia tri la: {cos_taylor(x)}, sai so {abs(cos_taylor(x) - math.cos(x))}')
print(f'Gia tri la: {sin_taylor(x)}, sai so {abs(sin_taylor(x)-math.sin(x))}') 

