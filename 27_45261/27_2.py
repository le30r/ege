f = open("107_27_B.txt")
n = int(f.readline())

elems = [0 for i in range(n)]

answers = [0 for i in range(n)]

sum = 0
rightSum = 0
leftSum = 0

for i in range(0,n):
    elems[i] = int(f.readline()) * 3

for i in range(1, n // 2): # центр в нуле
    sum += elems[n - i] * i + elems[i] * i

    rightSum += elems[i]
    leftSum += elems[n - i]
sum = sum + elems[n // 2] * n // 2
answers[0] = sum

for i in range(1, n):
    answers[i] = answers[i - 1] + leftSum + elems[i - 1] - rightSum - elems[(i + (n // 2) - 1) % n]
    rightSum = rightSum - elems[i] + elems[(i + (n // 2) - 1) % n]
    leftSum = leftSum - elems[(i + (n // 2)) % n] + elems[i - 1]
print(min(answers))