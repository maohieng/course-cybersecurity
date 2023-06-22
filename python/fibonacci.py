def fibonacci(n):
    if n < 1:
        print('n must be greater than 1')
        pass
    a=[0,1]
    for x in range (2, n+1):
        u = a[x - 1] + a[x -2]
        a.append(u)
    return a

n = int(input('Enter a series number of fibonacci: '))
print(fibonacci(n))