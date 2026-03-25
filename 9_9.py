f = open("09 (1).csv")

d = {}
arr = []
for s in f:
    s_nums = s.split(";")
    # 119;137;900;699;45;948 -> ["119", "137", "900","699", "45", "948"]
    nums = []
    for s_num in s_nums:
        num = int(s_num)
        d[num] = d.get(num, 0) + 1
        nums.append(num)
    arr.append(nums)
result = 0
for nums in arr:
    is_good = False
    for num in nums:
        if nums.count(num) == 1 and d[num] == 46:
            result += 1
            break

print(result)


