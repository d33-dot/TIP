#якубов денис эфбо-08-26
''' задание 1
n = int(input("введите число: "))
i = int(input("введите систему счисления числа: "))
print(int(str(n),i))
'''

''' задание 2
n = int(input("введите число: "))
i = int(input("введите систему счисления числа: "))
res = ''
while n != 0:
    res += str(n%i)
    n = n//i
print(res[::-1])
'''

"""# задание 3
n = int(input("введите число: "))
num = str(n)
i = int(input("введите систему счисления числа: "))
i2 = int(input("введите систему счисления для перевода: "))
res = ''
z=0
a=[]
if i == 10:
    while i2**z < n:
        a.insert(0,z)
        z+=1
    for x in a:
        b = max([z for z in range(0,i2) if (i2**x)*z <= n])
        res+=str(b)
        n = n-(i2**x)*b
else:
    n = int(str(n),i)
    while i2**z < n:
            a.insert(0,z)
            z+=1
    for x in a:
        b = max([z for z in range(0,i2) if (i2**x)*z <= n])
        res+=str(b)
        n = n-(i2**x)*b
if int(res,i2) == int(num,i):
    print(f'перевод успешен, результат: {res}')
else:
    print('ошибка')
"""

'''# задание 4
n = str(input("введите число: "))
i = int(input("введите систему счисления числа: "))
i2 = int(input("введите систему счиления для перевода: "))

if i2 == 10 and i != 10:
    res = (int(n, i))
elif i == 10 and i2 not in [0,1]:
    num = int(n) 
    res = ''
    if num == 0:
        res = '0'
    while num != 0:
        res += str(num % i2)
        num = num // i2
    res = res[::-1]
else:
    num = int(n, i)
    res = ''
    if num == 0:
        res = '0'
    while num != 0:
        res += str(num % i2)
        num = num // i2
    res = res[::-1]
print(res)
'''

''' задание 5
n = str(input("введите число: "))
i = int(input("введите систему счисления числа: "))
i2 = int(input("введите систему счиления для перевода: "))

if i2 == 10 and i != 10:
    res = str(int(n, i)) 

elif i == 10 and i2 not in [0,1]:
    num = int(n) 
    res = ''
    if num == 0:
        res = '0'
    while num != 0:
        res += str(num % i2)
        num = num // i2
    res = res[::-1]

else:
    num = int(n, i)
    res = ''
    if num == 0:
        res = '0'
    while num != 0:
        res += str(num % i2)
        num = num // i2
    res = res[::-1]

print("результат перевода:", res)

if i == 10:
    n1 = int(n)
else:
    n1 = int(n, i)

if i2 == 10:
    n2 = int(res)
else:
    n2 = int(res, i2)

if n1 == n2:
    print("обратное преобразование совпало")
else:
    print("обратное преобразование не совпало")
'''

''' задание 6
n = int(input('введите число: '))
a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print('основание | длина числа')
for b in range(2,37):
    x = n
    res = ''

    if x == 0:
        res='0'
    while x != 0:
        res+=a[x%b]
        x=x//b

    l = len(res)
    print(f'{b} | {l}')
'''

"""#задание 7
n = int(input('введите число: '))
a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mxl=[0,0]
mnl=[100,0]
prevl=0
changes=0
startl=len(str(n))
for b in range(2,37):
    x = n
    res=''

    if x == 0:
        res = '0'
    while x!=0:
        res+=a[x%b]
        x = x//b
    res = res[::-1]

    l = len(res)
    
    mxl=max(mxl,[l,b])
    mnl=min(mnl,[l,b])
    if prevl != 0 and prevl != l:
        changes += 1
    prevl = l
finl = int(len(res))

print(F'число {n} --> {res}')
print(f'длина записи {startl} --> {finl} изменилась в примерно {startl//finl} раз')
print(f'максимальная длина/СС {mxl}, минимальная длина/СС {mnl}')
print(f'длина изменилась {changes} раз')
"""

""" задание 8
n = str(input('введите число: ')).upper()
i = int(input('введите основание: '))
a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:i]
if n.startswith('-'):
    n = n[1:]

if len(n) < 1:
    print('нет числа для проверки')    
elif all(z in a for z in n):
    print('число подходит под систему счисления')
else:
    print('число не подходит под систему счисления')
"""