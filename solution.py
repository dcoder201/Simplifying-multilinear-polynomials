import re
def simplify(poly):
    pattern = re.compile(r'(?<=[a-z])(?=[\+\-])|(?<=[\+\-])(?=[a-z])|(?<=[0-9])(?=[a-z])')
    poly = re.sub(pattern, ' ', poly)
    cut = re.split(' ', poly)
    dic = {}
    for i in range(len(cut)):
        if not cut[i].isalpha():
            if cut[i] == '+':
                cut[i] = 1
            elif cut[i] == '-':
                cut[i] = -1
            else:
                cut[i] = int(cut[i])
        else:
            cut[i] = ''.join(sorted(cut[i]))
            if cut[i] not in dic:
                if i == 0:
                    dic[cut[i]] = 1
                else:
                    dic[cut[i]] = cut[i-1]
            else:
                dic[cut[i]] += cut[i-1]
    list1 = sorted(dic.items(), key=lambda x: (len(x[0]), x[0]))
    res = ''
    for each in list1:
        if each[1] == -1:
            res += '-' + each[0]
        elif each[1] == 0:
            pass
        elif each[1] == 1:
            res += '+' + each[0]
        elif each[1] > 1:
            res += '+' + str(each[1]) + each[0]
        else:
            res += str(each[1]) + each[0]
    return res.strip('+')
