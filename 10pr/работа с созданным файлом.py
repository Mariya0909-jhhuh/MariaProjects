f = open(r'Mariya_Slepicheva_UB-31_vvod.txt', 'r')
a = []
for i in f:
    b = []
    s = i.split(' ')
    for j in s:
        if j == '\n':
            continue
        b.append(int(j))
    a.append(b)
print(a)
f.close()
for i in a:
    minimum = i.index(min(i))
    maximum = i.index(max(i))
    i[maximum], i[0] = i[0], i[maximum]
    i[minimum], i[-1] = i[-1], i[minimum]
l = open(r'Mariya_Slepicheva_UB-31_vivod.txt', 'w')
for i in a:
    for j in i:
        l.write(str(j))
        l.write(' ')
    l.write('\n')
l.close()