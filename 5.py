def determinant(mat):
    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    det = 0
    for col in range(len(mat)):
        minor = [row[:col] + row[col + 1:] for row in mat[1:]]
        det += ((-1) ** col) * mat[0][col] * determinant(minor)
    return det

n = int(input())
mat = []

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(int(input()))
    mat.append(tmp)

for i in range(n):
    print(*mat[i])

print(determinant(mat))