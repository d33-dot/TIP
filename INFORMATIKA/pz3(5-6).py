# ФАЙЛ 1

''' задание 1
n = str(input())
l = len(n)
if int(n) == sum([int(i)**l for i in n]):
    print(f'число {n} является числом армстронга')
else:
    print(f'число {n} не является числом армстронга')
'''

''' задание 2
n = int(input())
def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibonacci=[0,1]
    for i in range(2,n):
        num = fibonacci[-1]+fibonacci[-2]
        fibonacci.append(num)
    return fibonacci

print(fib(n))
'''

''' задание 3
n = int(input())
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def genlist(n):
    return [fib(i) for i in range(n)]
res = genlist(n)
print(res)
'''

''' задание 4
n = int(input())
def factor(n):
    if n < 0:
        raise ValueError('')
    elif n==0 or n==1:
        return 1
    return n*factor(n-1)
print(f'факториал числа {n} = {factor(n)}')
'''

''' задание 5
s = str(input())
def counter(s):
    al = [i for i in set(s)]
    res = []
    for i in al:
        res.append([f'{i} встречается {s.count(i)} раз'])
    return res
print(*[i for i in counter(s)])
'''

''' задание 6
import random
n = int(input())
l = [random.randint(1,10) for _ in range(20)]
res=[]

for i in range(len(l)-1):
    for i2 in range(i+1 ,len(l)):
        if l[i] + l[i2] == n:
            pair = tuple(sorted( (l[i],l[i2]) ))
            if pair not in res:
                res.append(pair)
print(f'список: {l}')
print(res)
'''

#ФАЙЛ 2

# a = int(input())
# b = int(input())

# def mod8(n):
#     return n % 256

# def t(n):
#     return mod8(n)

# def add8(x, y):
#     while y:
#         c = x & y
#         x = x ^ y
#         y = c < 1
#     return mod8(x)

# def sub8(x, y):
#     return add8(x, add8(mod8(~y), 1)) # ~y = -(y+1) 3

# def mul8(x, y):
#     return mod8(x * y)

# def s(x):
#     return x - 256 if x >= 128 else x

# x = t(a)
# y = t(b)

# print("Сложение:", add8(x, y), bin(add8(x, y)))
# print("Вычитание:", sub8(x, y), bin(sub8(x, y)))
# print("Умножение:", mul8(x, y), bin(mul8(x, y)))


# print("Сложение:", s(add8(x, y)))
# print("Вычитание:", s(sub8(x, y)))
# print("Умножение:", s(mul8(x, y)))

#ФАЙЛ 3
'''
a = bin(132)[2:]
while len(a) <= 16:
    a = '0'+str(a)
print(a)
'''

'''
mn=0
mx=2**16-1
print(mn,mx)
'''

'''
n=12
k=8
b=bin(n)[2:].zfill(k-1)
d = '0'+b
b='0'+b
a='0'+b

print(f'прямой код: {d}')
print(f'обратный код: {b}')
print(f'дополнительный код: {a}')
'''

'''
n=-35
k=8
b=bin(abs(n))[2:].zfill(k-1)
print(b)
d='1'+b
b = '1'+''.join('1' if c == '0' else '0' for c in b)
a = bin(int(b,2)+1)[2:].zfill(k)

print(f'прямой код: {d}')
print(f'обратный код: {b}')
print(f'дополнительный код: {a}')
'''

'''
print("(A-B)ок =", bin(78 - 56)[2:].zfill(8))
print("(B-A)дк =", bin((56 - 78) & 255)[2:].zfill(8))
'''


#ТЕСТ
'''
1 - B
2 - C
3 - A
4 - A 
5 - B 
6 - A 
7 - D 
8 - B 
9 - A 
10 - 103 = 01100111 - прямой 1,1100111 - обратный 1,0011000 - доп. 10011001
'''

'''
import math
x = float(input('x: '))
y = float(input('y: '))
f = math.log(abs(math.sin(x+y)))
print(f)
'''

'''
import math
x = float(input('x: '))
y = float(input('y: '))
s = math.sin(x + y)
if s <= -0.5:
    f = math.atan((3 * x - y) ** (1 / 3))
elif s >= 0.5:
    f = x ** 3 + y ** 1.5
else:
    f = math.sqrt(3) * math.log(math.fabs(x * y), 3)
print('f =', f)
'''

'''
import math
a = float(input('a: '))
b = float(input('b: '))
h = float(input('h: '))
x = a
while x <= b:
    f = math.cos(math.e * x) ** 3 + math.sin(abs(x))
    print(f'x = {x:.3f}  f = {f:.3f}')
    x += h
'''

'''
import math
x = 1
while x <= 2.5:
    y = 1
    while y <= 4:
        if x + y <= 2:
            f = math.sin(x * math.exp(0.1 * y)) ** (1/3)
        else:
            f = math.log2(x + y)
        print(x, y, f)
        y += 1
    x += 0.5
'''