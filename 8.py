w, h = map(int, input().split())
mat = []

for i in range(h):
    row = input()
    temp = []
    for j in row:
        temp.append(j)
    mat.append(temp)

new_mat = []

for i in range(w):
    temp = []
    for j in mat:
        temp.append(j[i])
    new_mat.append(temp)

mat = []

for i in new_mat: 
    temp = []   
    for j in i:
        temp.append(j)
        temp.append(j)
    mat.append(temp)

for i in mat:
    i = ''.join(i)
    print(i)
    print(i)
