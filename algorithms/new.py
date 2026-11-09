a, b = int(input()), int(input())
import math
'''
while a!=0 and b!=0:
    if a > b:
        a = a%b
    else:
        b = b%a

print(f'{a + b}')
'''

'''
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

print(gcd(a,b))
'''

'''
def extended(a,b):
    if b == 0:
        return (g,1,0)
    g,x1,y1 = extended(b,a%b)
    x = y1
    y = x1 - (a//b)*y1
    return (g,x,y)

print(extended())
'''

'''
def naive_factorize(n):
    factors=[]
    for i in range(2,n+1):
        while n % i==0:
            factors.append(i)
            n= n//i
    return factors

print(naive_factorize(100))
'''

'''
# алгоритм Ферма n = a^2 - b^2 = (a-b)(a+b)
def ferma_factorize(n):
    if n % 2 == 0:
        return (2,n//2)
    a = math.isqrt(n)
    if a*a < n:
        a+=1
    while True:
        b2 = a*a-n
        b = math.isqrt(b2)
        if b*b==b2:
            factor1 = a-b
            factor2 = a+b
            return(factor1,factor2)
        a+=1

n1= 200819
f1,f2 = ferma_factorize(n1)

print(f'для n1 = {n1}')
print(f'найдены делители{f1,f2}')
'''