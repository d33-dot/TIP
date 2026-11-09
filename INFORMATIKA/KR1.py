#Якубов Денис ЭФБО-08-26

# задание 1
'''
import math

n = 26
length = 10

bits = math.ceil(math.log2(n))

total_bits = bits * length

print(f"минимальное число бит на букву: {bits} бит")
print(f"объем слова из {length} букв: {total_bits} бит")
'''
# задание 2
'''
oct_str = "77"

dec_num = int(oct_str, 8)
bin_str = bin(dec_num)[2:]

ones = bin_str.count('1')
is_odd = ones % 2 != 0

print(f"число {oct_str} в двоичной системе: {bin_str}")
print(f"количество единиц: {ones}")
print(f"проверка на нечётность: {'выполнена (нечётное)' if is_odd else 'не выполнена (чётное)'}")
'''

# задание 3
'''
a = 0x1234
b = 0xFEDC

total_sum = a + b

result = total_sum & 0xFFFF

carry = 1 if total_sum > 0xFFFF else 0

sign_a = (a >= 0x8000)
sign_b = (b >= 0x8000)
sign_res = (result >= 0x8000)

if sign_a == sign_b and sign_a != sign_res:
    overflow = 1
else:
    overflow = 0

print("Результат в HEX:", hex(result))
print("Флаг переноса (Carry Flag):", carry)
print("Флаг переполнения (Overflow Flag):", overflow)
'''

# задание 4
'''
bytes_data = [
    0xAA, 0x55, 0x01, 0x05, 0xFF,
    0xAA, 0x55, 0x00, 0x02, 0xFF,
    0xAA, 0x55, 0x01, 0x09, 0xFF
    ]

packs = 0

for i in range(len(bytes_data) - 2):
    if bytes_data[i] == 0xAA and bytes_data[i+1] == 0x55:
        if bytes_data[i+2] == 0x01:
            packs += 1

print("количество пакетов с little-endian порядком:", packs)
'''

# дополнительное
'''
dividend_raw = 239 
divisor_raw = 5

sign_div = (dividend_raw >> 7) & 1
abs_dividend = (~dividend_raw + 1) & 0xFF if sign_div else dividend_raw

sign_cls = (divisor_raw >> 7) & 1
abs_divisor = (~divisor_raw + 1) & 0xFF if sign_cls else divisor_raw

quotient = 0
remainder = abs_dividend

while remainder >= abs_divisor:
    remainder -= abs_divisor
    quotient += 1

if sign_div != sign_cls:
    quotient = (~quotient + 1) & 0xFF

if sign_div == 1:
    remainder = (~remainder + 1) & 0xFF

print("Частное (Quotient): ", bin(quotient)[2:].zfill(8))
print("Остаток (Remainder):", bin(remainder)[2:].zfill(8))
'''