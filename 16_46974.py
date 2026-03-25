# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:
#
# F(0)=0;
#
# F(n)=F(n − 1)+1, если n нечётно;
#
# F(n)=F(n / 2), если n > 0 и при этом n чётно.
#
# Укажите количество таких значений n<1000000000, для которых F(n)=2.

# f(10) = 2
# f(2) = 1
# f(4) = 1
# f(5) = 2

# memory = { 0: 0 }
#
# n = 5
# def f(n):
#     if n in memory:
#         return memory[n]
#
#     if n % 2 != 0:
#         m = n - 1
#         if m in memory:
#             v = memory[m]
#         else:
#             v = f(m)
#             memory[m] = v
#         return v + 1
#     if n > 0 and n % 2 == 0:
#         m = n / 2
#         if m in memory:
#             return memory[m]
#         else:
#             v = f(m)
#             memory[m] = v
#             return v
#
#     return 0
#
# k = 0
# for i in range(0, 100):
#     v = f(i)
#     memory[i] = v
#     print(i, v, bin(i).lstrip("0b"))
#
# print(k)


k = 0
for i in range(2, 31):
    k = k + i - 1
print(k)