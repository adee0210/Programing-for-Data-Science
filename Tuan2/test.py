def number_sum(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

n = int(input('Nhap gia tri n: '))
print(f'Sum is: {number_sum(n)}')