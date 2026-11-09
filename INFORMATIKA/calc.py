import string

DIGITS = string.digits + string.ascii_uppercase

def char_to_val(c, base):
    val = DIGITS.index(c.upper())
    if val >= base:
        raise ValueError(f"Символ '{c}' недопустим для системы счисления {base}.")
    return val

def val_to_char(val):
    return DIGITS[val]

def validate_number(num_str, base):
    if not num_str:
        return False
    for c in num_str:
        if c.upper() not in DIGITS or DIGITS.index(c.upper()) >= base:
            return False
    return True

def clean_leading_zeros(s):
    s = s.lstrip('0')
    return s if s else '0'

def compare_numbers(num1, num2):
    n1 = clean_leading_zeros(num1)
    n2 = clean_leading_zeros(num2)
    if len(n1) > len(n2):
        return 1
    if len(n1) < len(n2):
        return -1
    for c1, c2 in zip(n1, n2):
        v1 = DIGITS.index(c1.upper())
        v2 = DIGITS.index(c2.upper())
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
    return 0

def add_base(num1, num2, base):
    num1 = num1.upper()
    num2 = num2.upper()
    
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = []
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        d1 = char_to_val(num1[i], base)
        d2 = char_to_val(num2[i], base)
        
        current_sum = d1 + d2 + carry
        carry = current_sum // base
        result.append(val_to_char(current_sum % base))
        
    if carry:
        result.append(val_to_char(carry))
        
    return "".join(reversed(result))

def sub_base(num1, num2, base):
    if compare_numbers(num1, num2) < 0:
        raise ValueError("Ошибка: Результат вычитания не должен быть меньше 0.")
        
    num1 = num1.upper()
    num2 = num2.upper()
    
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = []
    borrow = 0
    
    for i in range(max_len - 1, -1, -1):
        d1 = char_to_val(num1[i], base)
        d2 = char_to_val(num2[i], base)
        
        diff = d1 - d2 - borrow
        if diff < 0:
            diff += base
            borrow = 1
        else:
            borrow = 0
            
        result.append(val_to_char(diff))
        
    res_str = "".join(reversed(result))
    return clean_leading_zeros(res_str)

def mul_base(num1, num2, base):
    num1 = clean_leading_zeros(num1.upper())
    num2 = clean_leading_zeros(num2.upper())
    
    if num1 == '0' or num2 == '0':
        return '0'

    running_total = '0'
    
    for i in range(len(num2) - 1, -1, -1):
        d2 = char_to_val(num2[i], base)
        current_product = []
        carry = 0
        
        for j in range(len(num1) - 1, -1, -1):
            d1 = char_to_val(num1[j], base)
            prod = d1 * d2 + carry
            carry = prod // base
            current_product.append(val_to_char(prod % base))
            
        if carry:
            current_product.append(val_to_char(carry))
            
        prod_str = "".join(reversed(current_product)) + '0' * (len(num2) - 1 - i)
        running_total = add_base(running_total, prod_str, base)
        
    return clean_leading_zeros(running_total)

def main():
    try:
        base = int(input("Введите основание системы счисления (2-36): "))
        if not (2 <= base <= 36):
            print("Ошибка: Основание должно быть в диапазоне от 2 до 36.")
            return
    except ValueError:
        print("Ошибка: Основание должно быть целым числом.")
        return

    num1_str = input("Введите первое число: ").strip()
    num2_str = input("Введите второе число: ").strip()
    operation = input("Введите операцию (+, -, *): ").strip()

    if not validate_number(num1_str, base):
        print(f"Ошибка: Число '{num1_str}' не соответствует системе счисления с основанием {base}.")
        return
    if not validate_number(num2_str, base):
        print(f"Ошибка: Число '{num2_str}' не соответствует системе счисления с основанием {base}.")
        return

    try:
        if operation == '+':
            res = add_base(num1_str, num2_str, base)
        elif operation == '-':
            res = sub_base(num1_str, num2_str, base)
        elif operation == '*':
            res = mul_base(num1_str, num2_str, base)
        else:
            print("Ошибка: Неподдерживаемая операция. Используйте только +, - или *.")
            return
            
        print(f"Результат в {base}-ичной СС: {res}")
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()