def solve(n, start):
    if n == 1:
        if start == 0:
            return 1
        if start == 1 or start == 3 or start == 7 or start == 9:
            return 2
        if start == 2 or start == 4 or start == 6:
            return 3
        if start == 5 or start == 8:
            return 4
    
    if start == 0:
        return solve(n - 1, 8)
    if start == 1:
        return solve(n - 1, 2) + solve(n - 1, 4)
    if start == 2:
        return solve(n - 1, 1) + solve(n - 1, 3) + solve(n - 1, 5)
    if start == 3:
        return solve(n - 1, 2) + solve(n - 1, 6)
    if start == 4:
        return solve(n - 1, 1) + solve(n - 1, 5) + solve(n - 1, 7)
    if start == 5:
        return solve(n - 1, 2) + solve(n - 1, 4) + solve(n - 1, 6) + solve(n - 1, 8)
    if start == 6:
        return solve(n - 1, 3) + solve(n - 1, 5) + solve(n - 1, 9)
    if start == 7:
        return solve(n - 1, 4) + solve(n - 1, 8)
    if start == 8:
        return solve(n - 1, 5) + solve(n - 1, 7) + solve(n - 1, 9) + solve(n - 1, 0)
    if start == 9:
        return solve(n - 1, 4) + solve(n - 1, 8)
    
n = int(input())
if n == 1 or n == 2:
    print(1)
else:
    print(solve(n - 2, 8))