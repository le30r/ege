# Пусть M  — максимальный простой натуральный делитель целого числа, не считая самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю.
# 
# Напишите программу, которая перебирает целые числа, большие 1 825 000,
# в порядке возрастания и ищет среди них такие, для которых M не больше 25 000 и оканчивается на 3.
#
# В ответе запишите первые пять найденных чисел в порядке возрастания.
# 
# Например, для числа 105 M  =  7.

# находит числа у которых есть делители оканчивающиеся на 3 и не больше 250000

import math

def is_prime(n): # является ли число простым
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_dividers(n):
    result = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                result.append(i)
            if is_prime(n // i):
                result.append(n // i)
    return result


k = 0
for n in range(1_825_001, 1_825_001 + 100000):
    dividers = prime_dividers(n)
    if len(dividers) != 0:
        M = max(dividers)
        if M % 10 == 3 and M < 25001:
            print(n)
            k += 1
    if k == 5:
        break