from random import randint
n = int(input())
m = int(input())
a = []
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,50))
    a.append(b)
f = open(r'Mariya_Slepicheva_UB-31_vvod.txt', 'w')
for i in a:
    for j in i:
        f.write(str(j))
        f.write(' ')
    f.write("\n")
f.close()