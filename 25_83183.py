# Пусть S  — сумма всех простых натуральных делителей целого числа, не считая самого числа.
# Если таких делителей у числа нет, то считаем значение S равным нулю.
# 
# Напишите программу, которая перебирает целые числа, меньшие 1 475 000,
# в порядке убывания и ищет среди них такие, для которых значение S не равно нулю,
# не больше 42 000 и кратно 6. В ответе запишите первые пять найденных чисел в порядке убывания.
# 
# Например, для числа 10S  =  2 + 5  =  7.
import math

def is_prime(n): # является ли число простым
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dividers(n):
    result = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                result.append(i)
            if is_prime(n // i):
                result.append(n // i)
    return result

c = 0
for i in range(1475000 - 1, 0, -1):
    d = dividers(i)
    if len(d) > 0:
        s = sum(d)
        if s < 42000 and s % 6 == 0:
            print(i)
            c += 1
            if c == 5:
                break
