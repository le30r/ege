#На числовой прямой даны два отрезка: P=[130; 171] и Q=[150; 185]. Укажите наименьшую возможную длину такого отрезка A,
# что формула
#(x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
#истинна при любом значении переменной х, т.е. принимает значение 1 при любом значении переменной х.

P = [i for i in range(130, 172)]
Q = [i for i in range(150, 186)]
m = 99999
for Amin in range(0,500):
    for Amax in range(Amin + 1, 500):
        A = [i for i in range(Amin, Amax)]
        k = 0
        for x in range(0, 700):
            if (x in P) <= (((x in Q) and (not (x in A))) <= (not (x in P))) == 1:
            #if not (x in P) or not (x in Q) or (x in A):
                k += 1
        if k == 700:
            m = min(m, Amax - Amin - 1)
print(m)


# (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P))
# x ∈ P
# A -> ((B ^ ~C) -> ~A)
# ~A v ((B ^ ~C) -> ~A)
# ~A v (~(B ^ ~C) v ~A)
# ~A v ~B v C
# ~(x ∈ P) v ~(x ∈ Q) v (x ∈ A)
# <130 v >171
# <150 v >185

