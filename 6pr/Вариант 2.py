#1
n=int(input())
n=[int(input()) for i in range(n)]
print(min(n))
print(n.index(min(n)))
#2
n=int(input())
n=[int(input()) for i in range(n)]
p=[]
o=[]
for j in range(len(n)):
    if n[j]>0:
        p.append(n[j])
    else:
        o.append(n[j])
print(p)
print(o)