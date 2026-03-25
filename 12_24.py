s = '0' + '1' * 12 + '2' * 15 + '3' * 17
print(s)
while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '103', 1)
    s = s.replace('02', '10', 1)
    s = s.replace('03', '210', 1)
print(s)
print(s.count("2"))
