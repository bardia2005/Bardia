dic = input()
if dic == '{}':
    print('{}')
else:
    temp = "{"
    for i in range(1, len(dic)):
        if dic[i] == ',' and dic[i - 1] == ']':
            temp += ':'
        else:
            temp += dic[i]

    temp = temp.replace('{', '')
    temp = temp.replace('}', '')
    temp = temp.replace('"', '')
    temp = temp.split(':')

    dic = {}
    for i in range(len(temp)):
        temp[i] = temp[i].strip()
        if i % 2 == 0:
            dic[temp[i]] = 1
        else:
            li = []
            for j in temp[i]:
                if ord(j) >= 48 and ord(j) <= 57:
                    li.append(int(j))
            dic[temp[i - 1]] = li


    li_keys = []
    li_values = []
    final_dic = {}

    for i in dic.values():
        for j in i:
            if j not in li_keys:
                li_keys.append(j)

    li_keys.sort()

    for i in li_keys:
        temp = []
        for j in dic.keys():
            if i in dic[j]:
                temp.append(j)
        li_values.append(temp)

    for i in range(len(li_keys)):
        final_dic[li_keys[i]] = li_values[i]

    s = str(final_dic)
    s = s.replace('"', '')
    print(s)