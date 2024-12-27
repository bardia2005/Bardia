def inv(n):
    if n == 1:
        return 0
    return 1

n = int(input())
state = input()

li = []

for i in range(n):
    nums = list(map(int, input().split()))
    li.append(nums)

mat = []

for i in range(n):
    temp = []
    current = int(state[i])
    for j in range(1000):
        if j < li[i][1]:
            temp.append(current) 
        elif j == li[i][1]:
            current = inv(current)
            temp.append(current)
        elif (j - li[i][1]) % li[i][0] == 0:
            current = inv(current)
            temp.append(current)
        else:
            temp.append(current)

    mat.append(temp)

Max = 0

for i in range(1000):
    cnt = 0
    for j in range(n):
        if mat[j][i]:
            cnt += 1
    if cnt > Max:
        Max = cnt

print(Max)