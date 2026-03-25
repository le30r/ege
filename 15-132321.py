#На числовой прямой даны два отрезка: P=[23, 58] и Q=[1, 39].
#Какова наименьшая возможная длина интервала A, что формула
#((x ∈ P) ∨ (x ∈ А)) → ((x ∈ Q) ∨ (x ∈ А))
#тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

P = [i for i in range(23, 59)]
Q = [i for i in range(1, 40)]
m = 999999
for Amin in range(0,100):
    for Amax in range(Amin + 1, 100):
        A = [i for i in range(Amin, Amax)]
        k = 0
        for x in range(0,300):
            if (((x in P) or (x in A)) <= ((x in Q) or (x in A))) == 1:
                k += 1
        if k == 300:
            m = min(m, Amax-Amin)
print(m)