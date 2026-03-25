# На числовой прямой даны два отрезка: P=[10, 29] и Q=[13, 18].
# Укажите наибольшую возможную длину отрезка A, для которого выражение
# ((x ∈ A) → (x ∈ P)) ∨ (x ∈ Q)
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.

P = [i for i in range(10, 30)]
Q = [i for i in range(13, 19)]
m = 0
for Amin in range(0, 100):
    for Amax in range(Amin + 1, 100):
        A = [i for i in range(Amin, Amax)]
        k = 0
        for x in range(0, 300):
            if ((x in A) <= (x in P)) or (x in Q) == 1:
                k += 1
        if k == 300:
            m = max(m, Amax - Amin - 1)
print(m)
