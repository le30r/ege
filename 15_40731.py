P = [i for i in range(19, 85)]
Q = [i for i in range(4, 52)]
m = 100 * 10
for Astart in range(0, 100):
    for Aend in range(Astart + 1, 100):
        A = [i for i in range(Astart, Aend)]
        k = 0
        for x in range(-100, 100):
            if not (x in Q) or (x in P) or (x in A):
                k += 1
        if k == 200:
            m = min(Aend - Astart, m)
print(m)
# (x ∈ Q) → (¬(x ∈ P) → ¬((x ∈ Q) ∧ ¬(x ∈ A)))
# x in Q =  q
# x in P = p
# x in A = a
#  q → (¬p -> ¬ ( q ∧ ¬ a))
# ~ q v (¬p -> ¬ ( q ∧ ¬ a))
# ~ q v (p v ¬ ( q ∧ ¬ a)
# ~ q v (p v ~ q v a)
# ~ q v p v a