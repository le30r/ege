alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(11, 36+1):
    for x in alphabet[1:p]:
        for y in alphabet[:p]:
            for z in alphabet[1:p]:
                if int(z+x, p) + int(x+y, p) == int(z+y+'A', p):
                        print(int(x+y+z, p))