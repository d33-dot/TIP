# Group: ЭФБО-08-26
# Student: Якубов Денис

import math

print("--- Задание 1 ---")
symbols = 16
one = int(math.log2(symbols))
length = 4
total = one * length
print(f"Символы 0-F, всего N = {symbols}")
print(f"I = log2({symbols}) = {one} бита на 1 символ")
print(f"Сообщение из {length} символов: {one} * {length} = {total} бит")
print(f"{total} бит = {total // 8} байта")
print(f"{total} в 16-ричной системе = {hex(total)}")
print()

print("--- Задание 2 ---")
print("F = (not A or B) and (C or A)")
print("A B C  F")
ones = 0
for i in range(8):
    a = i // 4
    b = i // 2 % 2
    c = i % 2
    f = ((1 - a) | b) & (c | a)
    if f == 1:
        ones += 1
        print(a, b, c, "", f, " <- F = 1")
    else:
        print(a, b, c, "", f)
print(f"Строк, где F = 1: {ones}")
print()

print("--- Задание 3 ---")


def f_task3(a: bool, b: bool, c: bool) -> bool:
    return a


errors = 0
for i in range(8):
    a = bool(i // 4)
    b = bool(i // 2 % 2)
    c = bool(i % 2)
    start = (a or (b and c)) and (a or (b and not c))
    if start != f_task3(a, b, c):
        errors += 1
print("F = (A or (B and C)) and (A or (B and not C)) = A")
print(f"Ошибок при проверке: {errors}")
print()

print("--- Задание 4 ---")


def charge(plugged, tariff_low, overheat):
    return plugged & tariff_low & (1 - overheat)


print("Charge = Plugged and TariffLow and not Overheat")
print("Plugged TariffLow Overheat -> Charge")
for i in range(8):
    p = i // 4
    t = i // 2 % 2
    o = i % 2
    print(f"{p} {t} {o} -> {charge(p, t, o)}")
print(f"Пример ввода: 1 1 0, вывод: {charge(1, 1, 0)}")
print(f"Пример ввода: 1 1 1, вывод: {charge(1, 1, 1)}")
print()

print("--- Задание 5 ---")
sets = [(0, 1, 0), (1, 0, 1), (1, 1, 0)]
names = ["x", "y", "z"]
terms = []
for s in sets:
    term = ""
    for j in range(3):
        if s[j] == 0:
            term += "¬" + names[j]
        else:
            term += names[j]
    terms.append(term)
print("СДНФ: f = " + " ∨ ".join(terms))
print("Минимальная: f = y¬z ∨ x¬yz")
errors = 0
for i in range(8):
    x = i // 4
    y = i // 2 % 2
    z = i % 2
    need = 1 if (x, y, z) in sets else 0
    res = (y & (1 - z)) | (x & (1 - y) & z)
    if res != need:
        errors += 1
print(f"Ошибок при проверке: {errors}")
print()

print("--- Задание 6 ---")


def mux(a: int, b: int, s0: int, s1: int) -> int:
    ns1 = 1 - s1
    ns0 = 1 - s0
    nb = 1 - b
    return (ns1 & (a | s0)) | (s0 & (a | b)) | (s1 & ns0 & nb)


print("I0 = A, I1 = 1, I2 = not B, I3 = A or B")
print("Y = ¬S1(A ∨ S0) ∨ S0(A ∨ B) ∨ S1¬S0¬B")
errors = 0
i = 0
while i < 16:
    a = i // 8
    b = i // 4 % 2
    s0 = i // 2 % 2
    s1 = i % 2
    inputs = [a, 1, 1 - b, a | b]
    real = inputs[s1 * 2 + s0]
    y = mux(a, b, s0, s1)
    if y != real:
        errors += 1
    print(f"A={a} B={b} S0={s0} S1={s1} -> Y={y}")
    i += 1
print(f"Ошибок при сравнении с мультиплексором: {errors}")
print()

print("--- Задание 7 ---")


def f_task7(a: int, b: int, c: int) -> int:
    return a | (b & c)


table = [0, 0, 0, 1, 1, 1, 1, 1]
print("F = A ∨ (B ∧ C)")
errors = 0
for i in range(8):
    a = i // 4
    b = i // 2 % 2
    c = i % 2
    f = f_task7(a, b, c)
    if f != table[i]:
        errors += 1
    print(f"{a}{b}{c} -> {f}")
print(f"Ошибок при сравнении с таблицей: {errors}")
