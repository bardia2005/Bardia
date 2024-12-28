def shape(path):
    rec = 0
    n = len(path)
    for i in range(n):
        x1, y1 = path[i]
        x2, y2 = path[(i + 1) % n]
        rec += (x1 * y2) - (x2 * y1)

    return rec

def find_dot(n, path):
    rec = shape(path)
    if rec > 0:
        direction = 270
    else:
        direction = 90

    ans = 0

    for i in range(n - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        if i + 2 < n:
            x3, y3 = path[i + 2]
        else:
            x3, y3 = path[0]

        way = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

        if (direction == 270 and way < 0) or (direction == 90 and way > 0):
            ans += 1

    return ans

n = int(input())
path = [tuple(map(int, input().split())) for i in range(n)]

print(find_dot(n, path))


