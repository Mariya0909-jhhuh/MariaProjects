m=int(input())
a=[]
summa=0
count=0
for i in range(m):
    b=[]
    for j in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print()
    for j in i:
        print(j, end='  ')
for i in range(m):
    for j in range(i+1, m):
        if a[i][j]>0:
            count+=1
            summa+=a[i][j]
print()
print(summa)
print(count)
