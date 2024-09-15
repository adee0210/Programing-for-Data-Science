import math
def sqrt(n):
    t = n
    while abs(t - n/t) > 10e-9:
        if t == n/t:
            return t
        else:
            t = (t+n/t)/2
        
    return t

n = int(input('Nhap gia tri n: '))
print(f'Ket qua:{sqrt(n)}, {abs(sqrt(n) - math.sqrt(n))}')            
