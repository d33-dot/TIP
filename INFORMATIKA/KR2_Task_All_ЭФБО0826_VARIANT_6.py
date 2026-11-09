# Group: ЭФБО-08-26
# Student: Якубов
# Variant: 6

import math

print("========================================")
print("ЗАДАНИЕ 1: Объем информации")
print("========================================")
# Условие: Шестнадцатеричный код (0-F). 
N = 16  
i = math.log2(N) # Количество информации одного символа
message_length = 4
I_bits = i * message_length
I_bytes = I_bits / 8

print(f"1 символ: {i:.0f} бит")
print(f"4 символа: {I_bits:.0f} бит = {I_bytes:.0f} байт\n")


print("========================================")
print("ЗАДАНИЕ 2: Таблица истинности")
print("========================================")
# Формула: F = (¬A ∨ B) ∧ (C ∨ A)
print("A B C | F")
print("-" * 9)
count_ones = 0
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            f = ((not a or b) and (c or a))
            if f:
                count_ones += 1
            print(f"{a} {b} {c} | {f}")
print(f"\nКоличество строк, где F = 1: {count_ones}\n")


print("========================================")
print("ЗАДАНИЕ 3: Упрощение логической функции")
print("========================================")
# Исходная: F = (A ∨ (B ∧ C)) ∧ (A ∨ (B ∧ ¬C))
# Минимизированная: F = A
def f3(a: bool, b: bool, c: bool) -> bool:
    return a

print(f"Проверка f3(True, False, True) = {f3(True, False, True)}")
print(f"Проверка f3(False, True, True) = {f3(False, True, True)}\n")


print("========================================")
print("ЗАДАНИЕ 4: Система зарядки электромобиля")
print("========================================")
# Условие: Charge = Plugged ∧ TariffLow ∧ ¬Overheat
def charge_car(plugged: int, tariff_low: int, overheat: int) -> int:
    # Возвращает 1, если все условия выполнены, иначе 0
    return int(plugged == 1 and tariff_low == 1 and overheat == 0)

p, t, o = 1, 1, 0
print(f"Входы: Plugged={p}, TariffLow={t}, Overheat={o}")
print(f"Выход Charge: {charge_car(p, t, o)}\n")


print("========================================")
print("ЗАДАНИЕ 5: СДНФ и минимизация")
print("========================================")
# Наборы: (0,1,0), (1,0,1), (1,1,0)
# Минимальная форма: f = (y ∧ ¬z) ∨ (x ∧ ¬y ∧ z)
def f5(x: int, y: int, z: int) -> int:
    return int((y and not z) or (x and not y and z))

print(f"f5(0, 1, 0) = {f5(0, 1, 0)}")
print(f"f5(1, 0, 1) = {f5(1, 0, 1)}")
print(f"f5(1, 1, 0) = {f5(1, 1, 0)}\n")


print("========================================")
print("ЗАДАНИЕ 6: Мультиплексор 4->1")
print("========================================")
# Вариант 6: I0 = A, I1 = 1, I2 = ¬B, I3 = A ∨ B
def mux(a: int, b: int, s0: int, s1: int) -> int:
    if s1 == 0 and s0 == 0: return a           # I0
    elif s1 == 0 and s0 == 1: return 1         # I1
    elif s1 == 1 and s0 == 0: return 1 - b     # I2 (¬B)
    elif s1 == 1 and s0 == 1: return int(a or b) # I3 (A ∨ B)

a_m, b_m, s0_m, s1_m = 1, 0, 1, 0
print(f"Входы: a={a_m}, b={b_m}, s0={s0_m}, s1={s1_m}")
print(f"Выход Y: {mux(a_m, b_m, s0_m, s1_m)}\n")


print("========================================")
print("ЗАДАНИЕ 7: Восстановление схемы")
print("========================================")
# Таблица истинности указывает на F = A ∨ (B ∧ C)
def f7(a: int, b: int, c: int) -> int:
    return int(a or (b and c))

print("Проверка таблицы истинности:")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            print(f"{a} {b} {c} -> {f7(a, b, c)}")