# На числовой прямой даны два отрезка: P=[25; 50] и Q=[32; 47]. Укажите наибольшую возможную длину промежутка A,
# для которого формула
# 
# (¬ (x in A) → (x in P)) → ((x in A) → (x in Q))
# 
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.
P = [i for i in range(25, 51)]
Q = [i for i in range(32, 48)]
m = 0
for Amin in range(0, 60):
    for Amax in range(Amin + 1, 60):
        A = [i for i in range(Amin, Amax)]
        k = 0
        for x in range(0, 300):
            if ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q)):
                k += 1
        if k == 300:
            m = max(m, Amax - Amin - 1)
print(m)