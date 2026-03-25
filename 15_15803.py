# На числовой прямой задан отрезок A. Известно, что формула
#
# ((x ∈ A) → (x ^ 2 ≤ 100)) ∧ ((x ^ 2 ≤ 64) → (x ∈ A))
# ->
# - v
# (x ∈ A) → (x ^ 2 ≤ 100) = ~(x ∈ A) v (x ^ 2 ≤ 100)
# (x ^ 2 ≤ 64) → (x ∈ A) = (x ^ 2 > 64) v (x ∈ A)
# тождественно истинна при любом вещественном x. Какую наибольшую длину может иметь отрезок A


def f(x, Astart, Aend):
    x_in_A = Astart <= x <= Aend
    return (x_in_A <= (x ** 2 <= 100)) and ((x ** 2 <= 64) <= x_in_A)

m = 0
for Astart in range(-200, 200):
    for Aend in range(Astart + 1, 200):
        k = 0
        for x in range(-500, 500):
            if f(x, Astart, Aend):
                k += 1

        if k == 1000:
            l = Aend - Astart
            m = max(l, m)
print(m)