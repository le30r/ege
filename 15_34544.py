#На числовой прямой даны два отрезка: P = [10, 39] и Q = [23, 58]. Какова наименьшая возможная длина интервала A,
# что формула
#((x ∈ P) ∧ (x ∈ Q)) → ((x ∈ Q) ∧ (x ∈ A))
#тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

P = [i for i in range(10,40)]
Q = [i for i in range(23,59)]
m = 10000
for Amin in range(0,100):
    for Amax in range(Amin + 1, 100):
        A = [i for i in range(Amin, Amax + 1)]
        k = 0
        for x in range(0,300):
            if (((x in P) and (x in Q)) <= ((x in Q) and (x in A))) == 1:
                k += 1
        if k == 300:
            print(Amin, Amax)
            m = min(m, Amax - Amin)
print(m)