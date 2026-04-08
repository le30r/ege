# Пусть M — сумма максимального и минимального простых делителей целого числа,
# не считая единицы и самого числа.
# Если у числа нет простых делителей,
# то считаем значение M равным нулю.
# Напишите программу, которая перебирает целые числа, большие 7 500 000,
# в порядке возрастания и ищет среди них первые пять таких чисел,
# для которых M заканчивается на 32 и кратно общему количеству простых делителей.

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

def dividers(n):
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result


c = 0
n = 7500001
while c < 5:
    pd = prime_dividers(n)
    if len(pd) > 0:
        mn = min(pd)
        mx = max(pd)
        s = mx + mn
        if s % 100 == 32 and s % len(pd) == 0:
            print(n)
            c += 1
    n += 1