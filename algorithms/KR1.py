import math
import bisect

def binary_search_and_insert(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2  
        if arr[mid] == key:
            return f"Элемент {key} найден на индексе: {mid}"
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    insert_idx = low
    arr.insert(insert_idx, key)
    return f"Элемент не найден. Вставлен на позицию {insert_idx}. Массив: {arr}"

def check_mountain_array(arr):
    if len(arr) < 3:
        return "Массив не горный"
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    peak = low
    if peak == 0 or peak == len(arr) - 1:
        return "Массив не горный"
    for i in range(peak):
        if arr[i] >= arr[i + 1]: 
            return "Массив не горный"
    for i in range(peak, len(arr) - 1):
        if arr[i] <= arr[i + 1]: 
            return "Массив не горный"
    return f"Массив горный. Индекс пика: {peak}"

def compare_positives_and_negatives(arr):
    n = len(arr)
    low, high = 0, n - 1
    first_non_negative = n
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= 0:
            first_non_negative = mid
            high = mid - 1
        else:
            low = mid + 1
    low, high = 0, n - 1
    first_positive = n
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > 0:
            first_positive = mid
            high = mid - 1
        else:
            low = mid + 1
    neg_count = first_non_negative
    pos_count = n - first_positive
    if pos_count > neg_count:
        return f"Положительных чисел больше. Их количество: {pos_count}"
    elif neg_count > pos_count:
        return f"Отрицательных чисел больше. Их количество: {neg_count}"
    else:
        return f"Поровну. Отрицательных: {neg_count}, Положительных: {pos_count}"

def count_smaller_chunks(nums):
    counts = []
    seen = []
    for x in reversed(nums):
        idx = bisect.bisect_left(seen, x)
        counts.append(idx)
        bisect.insort(seen, x)
    return list(reversed(counts))

def f_variant_1(x):
    return math.exp(x - 1) - x**3 - x  

def bisection_solver(f, L, R, eps=0.0001):
    if f(L) * f(R) > 0:
        return "Нет корней или нарушена монотонность"
    shag = 0
    while (R - L) > eps:
        shag += 1
        B = L + (R - L) / 2
        if f(L) * f(B) < 0:
            R = B
        else:
            L = B
    return B

def chord_method_sqrt(A, eps=0.0001):
    def func(x): 
        return x * x - A
    a = 1.0
    b = float(A)
    x_prev = a
    k = 0
    while True:
        k += 1
        x_k = a - (func(a) * (b - a)) / (func(b) - func(a))
        if abs(x_k - x_prev) < eps:
            break
        if func(x_k) == 0:
            break
        if func(x_k) * func(b) > 0:
            b = x_k
        else:
            a = x_k
        x_prev = x_k
    return x_k

print("--- Тетрадь 1.2 Задание 1 ---")
print(binary_search_and_insert([1, 2, 4, 5], 3))

print("\n--- Тетрадь 1.2 Задание 2 ---")
print(check_mountain_array([1, 3, 5, 4, 2]))

print("\n--- Тетрадь 1.2 Задание 3 ---")
print(compare_positives_and_negatives([-3, -2, -1, 0, 1, 4, 5]))

print("\n--- Тетрадь 1.2 Задание 4* ---")
print(count_smaller_chunks([5, 2, 6, 1]))

print("\n--- Тетрадь 1 Задание 1 (Вариант 1) ---")
print(f"Корень: {bisection_solver(f_variant_1, 0.0, 1.0):.5f}")

print("\n--- Тетрадь 1 Задание 2 ---")
print(f"Квадратный корень из 16: {chord_method_sqrt(16):.5f}")
