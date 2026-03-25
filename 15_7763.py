# На числовой прямой даны два отрезка: P=[5, 30] и Q=[14, 23].
# Укажите наибольшую возможную длину промежутка A, для которого формула
#
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
#
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

P = [i for i in range(5, 31)] #5,30
Q = [i for i in range(14, 24)] #14,23
m = 0
for Amin in range(0, 100):
    for Amax in range(Amin + 1, 100):
        A = [i for i in range(Amin, Amax)]
        k = 0
        for x in range(0, 300):
            if (((x in P) == (x in Q)) <= (not(x in A))) == 1:
                k += 1
        if k == 300:
            m = max(m, Amax-Amin)
print(m)

