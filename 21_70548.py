def f(k, x):

    if (x == 3 or x == 5) and k <= 19: return True
    elif x == 5 and k > 19: return False
    elif k <= 19: return False


    if x % 2 == 0:
        return f(k - 2, x + 1) or f(k - 5, x + 1) or f(k // 3, x + 1)
    else:
        return f(k - 2, x + 1) and f(k - 5, x + 1) and f(k // 3, x + 1)

def f1(k, x):
    if x == 3 and k <= 19: return True
    elif x == 3 and k > 19: return False
    elif k <= 19: return False

    if x % 2 == 0:
        return f1(k - 2, x + 1) or f1(k - 5, x + 1) or f1(k // 3, x + 1)
    else:
        return f1(k - 2, x + 1) and f1(k - 5, x + 1) and f1(k // 3, x + 1)

for k in range(20, 100):
    if f(k, 1) == 1:
        print(k)
print("=======")
for k in range(20, 100):
    if f1(k, 1) == 1:
        print(k)