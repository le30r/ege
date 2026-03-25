# in - нашлось
# replace
sm_max = -1
for n in range(3, 4001):
    s = '1' + ('2' * n)
    while ('12' in s) or ('322' in s) or ('2222' in s):
        if '12' in s:
            s = s.replace('12', '2')
        if '322' in s:
            s = s.replace('322', '21')
        if '2222' in s:
            s = s.replace('2222', "3")
    sm = 0
    for i in s:
        sm += int(i)
    sm_max = max(sm_max, sm)
print(sm_max)