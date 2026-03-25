# 90  Кбайт >= x * ((102 + log2(x)) // 8 + 50)
import math

for x in range(1,10000):
    bits = 17 * 6 + math.log2(x)
    bytes = math.ceil(bits / 8)
    if (90 * 1024) >= (x * (bytes +21 50)):
        print(x)