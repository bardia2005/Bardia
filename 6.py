def solve(string):
    if string.isdigit():
        return [int(string)]
    li = []
    for i, char in enumerate(string):
        if char in "+-*":
            li_left = solve(string[:i])
            li_right = solve(string[i + 1:])
            
            for left in li_left:
                for right in li_right:
                    if char == '+':
                        li.append(left + right)
                    elif char == '-':
                        li.append(left - right)
                    elif char == '*':
                        li.append(left * right)
    
    return li

string = input().strip()
li = solve(string)
li = sorted(li)

for r in li:
    print(r)
