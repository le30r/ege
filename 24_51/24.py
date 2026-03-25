# Текстовый файл состоит из цифр 0, 6, 7, 8, 9 и знаков арифметических операций «−» и «*» (вычитание и умножение).
# Определите максимальное количество символов в непрерывной последовательности,
# которая является корректным арифметическим выражением с целыми неотрицательными числами.

# В этом выражении никакие два знака арифметических операций не стоят рядом,
# в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака.
#
# В ответе укажите количество символов.


f = open("demo_2025_24.txt")
s = f.readline()
nums = ["0", "6", "7", "8", "9"]
nums_without_zero = ["6", "7", "8", "9"]

signs = ["-", "*"]
k = 1
m = 0
n = len(s)
i = 0
while i < n:
    if not s[i] in nums:
        i += 1
        continue

    start = i
    prev_was_op = False
    valid = True

    while i < n:
        c = s[i]

        if c in nums:
            if c == "0":
                if i == start or s[i - 1] in signs:
                    if i + 1 < n and s[i + 1] in nums:
                        break
            prev_was_op = False
            i += 1
        elif c in signs:
            if prev_was_op:
                break
            prev_was_op = True
            i += 1
        else:
            break

    end = i

    if end > start and s[end - 1] in signs:
        end -= 1
    if end > start:
        m = max(m, end - start)

    i = start + 1
print(m)



# 7-99*09-00--88-*00*80*06---7-*0809*9*6*700-969**0