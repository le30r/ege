#Алгоритм вычисления значения функции F(a, b), где a и b— целые неотрицательные числа, задан следующими соотношениями:
#F(a, 0)=a;
#F(a, b)=F(a−1, b)+b, если a≥b;
#F(a, b)=F(a, b−1)+a, если a<b и b>0.
#Укажите количество таких целых неотрицательных чисел a, для которых можно подобрать такое b, что F(a, b)=1048576.
import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

def F(a, b):
    if b == 0:
        return a
    if a >= b:
        return F(a - 1, b) + b
    if a < b and b > 0:
        return F(a, b - 1) + a


print(F(3, 10))
print(F(3, 7))

c = 0
for a in range(1, 1_048_577):
    if 1_048_576 % a == 0:
        print(a)
        c += 1
print(c)



# a * b - 1

#F(a, 0)=a;
#F(a, b)=F(a−1, b)+b, если a≥b;
#F(a, b)=F(a, b−1)+a, если a<b и b>0.

# a = 5, b = 10 | 5 + 5 + 5 + 5 + 5 + 5 + 4 + 4 + 3 + 3 + 2 + 2 + 1 + 1 + 1
# a = 5, b = 9
# a = 5, b = 8
# a = 5, b = 7
# a = 5, b = 6
# a = 5, b = 5
# a = 4, b = 5
# a = 4, b = 4
# a = 3, b = 4
# a = 3, b = 3
# a = 2, b = 3
# a = 2, b = 2
# a = 1, b = 2
# a = 1, b = 1
# a = 1, b = 0