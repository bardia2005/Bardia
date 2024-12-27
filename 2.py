n = int(input())

enter = {}
out = {}
names = []

for i in range(n):
    name, time = input().split()
    if name in enter.keys():
        names.append(name)
        out[name] = int(time[0]) * 600 + int(time[1]) * 60 + int(time[3]) * 10 + int(time[4])
    else:
        enter[name] = int(time[0]) * 600 + int(time[1]) * 60 + int(time[3]) * 10 + int(time[4])


for i in range(n // 2):
    print(out[names[i]] - enter[names[i]])