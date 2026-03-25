res = []
for x in "0123456789ABCDE":
    for y in "0123456789ABCDE":
        A = "90" + x + "4" + y
        B = "91" + x + y + "2"
        result = int(A, 15) + int(B, 16)
        if result % 56 == 0:
            res.append(result)

print(min(res) // 56)
