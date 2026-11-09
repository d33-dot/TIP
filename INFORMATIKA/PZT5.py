''' задание 1
n = str(input('введите двоичное число: '))
a="01234567"
while len(n)%3!=0:
    n = '0'+n

res=''
for i in range(0,len(n),3):
    g = n[i:i+3]
    res += a[int(g,2)]
print(res)
'''

""" задание 2
n = str(input('введите двоичное число: '))
a="0123456789ABCDEF"

while len(n)%4!=0:
    n = '0'+ n

res=''
for i in range(0,len(n),4):
    g = n[i:i+4]
    res += a[int(g,2)]
print(res) 
"""

''' задание 3
n = str(input('введите восьмеричное число: '))
a='01234567'

b=''
for i in n:
    b += format(a.index(i),"03b")
print(b)
'''

''' задание 4
n = str(input('введите шестнадцатеричное число: ')).upper()
a="0123456789ABCDEF"

b=''
for i in n:
    b += format(a.index(i),'04b')
print(b)
'''

''' задание 5
n = str(input('введите число: ')).upper()
i = int(input('введите систему счисления числа: '))
i2 = 24-i
a="0123456789ABCDEF"
def binary(n,i,a="0123456789ABCDEF"):
    b=''
    bit = int.bit_length(i-1)

    for x in n:
        b += format(a.index(x),f"0{bit}b")
    return b

def change(n,i,a="0123456789ABCDEF"):
    res=''
    bit = int.bit_length(i-1)
    while len(n)%bit!=0:
        n='0'+n
    for x in range(0,len(n),bit):
        res += a[int(n[x:x+bit],2)]
    return res
    
binar = binary(n,i)
result = change(binar,i2)

print(result)
'''

''' задание 6
n = str(input('введите число: ')).upper()
i = int(input('введите систему счисления числа: '))
i2 = 24-i
a="0123456789ABCDEF"
def binary(n,i,a="0123456789ABCDEF"):
    b=''
    bit = int.bit_length(i-1)

    for x in n:
        b += format(a.index(x),f"0{bit}b")
    return b

def change(n,i,a="0123456789ABCDEF"):
    res=''
    bit = int.bit_length(i-1)
    while len(n)%bit!=0:
        n='0'+n
    for x in range(0,len(n),bit):
        res += a[int(n[x:x+bit],2)]
    return res

def check(n, res, i2):
    rev_bin = binary(res, i2)

    if n.lstrip('0') == rev_bin.lstrip('0'):
        return True
    return False

    
binar = binary(n,i)
result = change(binar,i2)
if check(binar,result,i2):
    print(f'значения сошлись: {result}')
else:
    print('значения не сошлись')
'''

''' задание 7
a = "0123456789ABCDEF"

def binary_correct(n, i):
    b = ''
    bit = int.bit_length(i - 1)
    for x in n:
        b += format(a.index(x), f"0{bit}b")
    return b

def change_correct(n, i):
    res = ''
    bit = int.bit_length(i - 1)
    while len(n) % bit != 0:
        n = '0' + n
    for x in range(0, len(n), bit):
        res += a[int(n[x:x + bit], 2)]
    return res

def binary_broken(n, i):
    b = ''
    for x in n:
        b += format(a.index(x), "b") 
    return b

oct_num = "50"  
print(f"1. перевод из 8-сс ({oct_num}) в 16-сс через 2-сс:")

bin_ok_8 = binary_correct(oct_num, 8)
hex_ok = change_correct(bin_ok_8, 16)

bin_bad_8 = binary_broken(oct_num, 8)
hex_bad = change_correct(bin_bad_8, 16)

print(f"с нулями:   {oct_num} -> двоичный: {bin_ok_8:7} -> 16-сс: {hex_ok}")
print(f"без нулей:  {oct_num} -> двоичный: {bin_bad_8:7} -> 16-сс: {hex_bad}")

hex_num = "A02" 
print(f"\n2. перевод из 16-сс ({hex_num}) в 8-сс через 2-сс:")

bin_ok_16 = binary_correct(hex_num, 16)
oct_ok = change_correct(bin_ok_16, 8)

bin_bad_16 = binary_broken(hex_num, 16)
oct_bad = change_correct(bin_bad_16, 8)

print(f"с нулями:   {hex_num} -> двоичный: {bin_ok_16:13} -> 8-сс: {oct_ok}")
print(f"без нулей:  {hex_num} -> двоичный: {bin_bad_16:13} -> 8-сс: {oct_bad}")

print("итог: из-за неправильного разбиения на биты при переводе без ведущих нулей, программа теряет смысл, резутльтат будет неправильным")
'''

#                       ЗАДАНИЕ 8
#вывод о преимуществах прямого метода перехода между системами счисления с основаниями степени двойки
#
#1. эффективность: программа не делает сложные математические операции для перевода, а только заменяет символы
#2. простота: программа пишется через простые циклы срезов строк
#3. точность: так как используется строка, то не может возникнуть ошибок из-за погрешностей или искажения данных при работе с огромными числами