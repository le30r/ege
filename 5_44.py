for n in range(0, 13):
    n_bin = bin(n).lstrip("0b")
    if n % 2 == 0:
        n_bin = "10" + n_bin
    else:
        n_bin = "1" + n_bin + "00"
    r = int(n_bin, 2)
    print(r)