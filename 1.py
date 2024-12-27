def find_squares(mat):
    rows = len(mat)
    cols = len(mat[0]) if rows > 0 else 0
    submatrices = []

    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submat = [row[j: j + size] for row in mat[i: i + size]]
                submatrices.append(submat)

    return submatrices

def is_zero(mat, n, m):
    Sum = 0
    for i in mat:
        Sum += sum(i)
    if not Sum:
        return True
    return False

n, m = map(int, input().split())
mat = []

for i in range(n):
    nums = list(map(int, input().split()))
    mat.append(nums)

li_subsquares = find_squares(mat)
li_subsquares = sorted(li_subsquares, key = len, reverse = True)
flag = 0

for i in li_subsquares:
    if is_zero(i, n, m):
        ans = i
        flag = 1
        break

if not flag:
    print(-1)
else:
    for i in ans:
        print(*i)