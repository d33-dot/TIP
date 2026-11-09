import math

def gcd_two(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_three(a, b, c):
    return gcd_two(gcd_two(a, b), c)

def gcd_four_subtraction(a, b, c, d):
    def gcd_sub(x, y):
        while x != y:
            if x > y:
                x -= y
            else:
                y -= x
        return x
    return gcd_sub(gcd_sub(gcd_sub(a, b), c), d)

def task_1_gcd(variant_type, numbers):
    if variant_type == "odd":
        a, b, c = numbers[:3]
        return f"НОД трех чисел методом деления: {gcd_three(a, b, c)}"
    else:
        a, b, c, d = numbers[:4]
        return f"НОД четырех чисел методом вычитания: {gcd_four_subtraction(a, b, c, d)}"

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def task_2_factorization(n):
    if n < 2:
        return "Факторизация невозможна для чисел меньше 2"
    primes = sieve_of_eratosthenes(n)
    factors = {}
    temp = n
    for p in primes:
        if p * p > temp:
            break
        if temp % p == 0:
            count = 0
            while temp % p == 0:
                count += 1
                temp //= p
            factors[p] = count
    if temp > 1:
        factors[temp] = 1
    res = " * ".join([f"{p}^{k}" if k > 1 else f"{p}" for p, k in factors.items()])
    return f"{n} = {res}"

def task_3_fermat_factorization(n):
    if n % 2 == 0 or n < 2:
        return "Метод Ферма применим только к нечетным числам >= 3"
    
    def fermat_step(num):
        if num < 2:
            return []
        if num in sieve_of_eratosthenes(num):
            return [num]
        m = math.isqrt(num)
        if m * m == num:
            return fermat_step(m) + fermat_step(m)
        x = 1
        while True:
            q = (m + x) * (m + x) - num
            koren_iz_q = math.isqrt(q)
            if koren_iz_q * koren_iz_q == q:
                break
            x += 1
            if (m + x) > (num + 1) // 2:
                return [num]
        factor1 = (m + x) - koren_iz_q
        factor2 = (m + x) + koren_iz_q
        return fermat_step(factor1) + fermat_step(factor2)

    all_prime_factors = fermat_step(n)
    factors = {}
    for f in all_prime_factors:
        factors[f] = factors.get(f, 0) + 1
    res = " * ".join([f"{p}^{k}" if k > 1 else f"{p}" for p, k in sorted(factors.items())])
    return f"{n} = {res}"

def task_4_lucas_lehmer(p):
    if p < 2:
        return f"M_{p} составное"
    if p == 2:
        return f"M_2 = 3 ПРОСТОЕ"
    primes = sieve_of_eratosthenes(p)
    if not primes or primes[-1] != p:
        return "Параметр p должен быть простым числом"
    M = (1 << p) - 1
    S = 4
    for _ in range(p - 2):
        S = (S * S - 2) % M
    if S == 0:
        return f"M_{p} = {M} ПРОСТОЕ"
    else:
        return f"M_{p} = {M} СОСТАВНОЕ"

def task_5_von_neumann(seed, count=10):
    res = []
    current = seed
    for _ in range(count):
        squared_str = str(current * current).zfill(10)
        start_idx = (len(squared_str) - 5) // 2
        current = int(squared_str[start_idx:start_idx + 5])
        res.append(current)
    return res

def task_6_sieve_of_sundaram(limit):
    if limit < 2:
        return []
    k = (limit - 1) // 2
    marked = [False] * (k + 1)
    for i in range(1, k + 1):
        for j in range(i, k + 1):
            val = i + j + 2 * i * j
            if val > k:
                break
            marked[val] = True
    primes = [2] if limit >= 2 else []
    for n in range(1, k + 1):
        if not marked[n]:
            primes.append(2 * n + 1)
    return primes

print("--- Задание 1 (Нечетный вариант, поиск НОД трех чисел делением) ---")
print(task_1_gcd("odd", [128, 96, 64]))

print("\n--- Задание 1 (Четный вариант, поиск НОД четырех чисел вычитанием) ---")
print(task_1_gcd("even", [128, 96, 64, 32]))

print("\n--- Задание 2 (Факторизация перебором с решетом Эратосфена) ---")
print(task_2_factorization(60))

print("\n--- Задание 3 (Факторизация нечетного числа методом Ферма) ---")
print(task_3_fermat_factorization(19691))

print("\n--- Задание 4 (Тест Люка-Лемера для чисел Мерсенна) ---")
print(task_4_lucas_lehmer(13))
print(task_4_lucas_lehmer(11))

print("\n--- Задание 5 (Генератор последовательности чисел фон Неймана) ---")
print(task_5_von_neumann(14563))

print("\n--- Задание 6* (Поиск простых чисел по алгоритму Решето Сундарамы) ---")
print(task_6_sieve_of_sundaram(100))
