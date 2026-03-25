#15
#На числовой прямой даны два отрезка: P=[130; 171] и Q=[150; 185]. Укажите наименьшую возможную длину такого отрезка A, что формула
#(x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
#истинна при любом значении переменной х, т.е. принимает значение 1 при любом значении переменной х.
P = [i for i in range(130,172)]
Q = [i for i in range(150, 186)]
m = 10 ** 6
for Amin in range(0, 250):
    for Amax in range(Amin + 1, 250):
        A = [i for i in range(Amin, Amax + 1)]
        k = 0
        for x in range(0, 500):
            if ((x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))) == 1:
                k += 1
        if k == 500:
            m = min(m, Amax - Amin)
print(m)